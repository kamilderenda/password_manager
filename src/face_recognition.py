from pathlib import Path
from typing import Union
import multiprocessing
from mtcnn.mtcnn import MTCNN
from keras.models import Model
from PIL import Image
import numpy as np
import cv2
from scipy.spatial.distance import cosine
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input

THRESHOLD = 0.5


class CameraNotFunctioning(AssertionError):
    pass


class FaceNotDetected(ValueError):
    """Thrown when no face is detected in an image"""
    pass


def create_model():
    return VGGFace(include_top=False, model='resnet50', input_shape=(224, 224, 3), pooling='avg')


def add_face(image: Image) -> None:
    """
    Adds face to the face directory with an index of the added user
    :param image:
    :return:
    """
    max_index = max([int(x.with_suffix("").name) for x in (Path(__file__).parent.parent / 'assets').iterdir()])
    target_path = Path(__file__).parent.parent / 'assets' / f'{max_index + 1}.jpg'
    image.save(str(target_path))


def check_saved(new_face: Image, image: Path, model: Model) -> Union[str, None]:
    """
    Checks all the saved users and returns a user's index if evaluation is True.
    If none of the evaluations is true returns None
    :param image:
    :param model:
    :param new_face:
    :return:
    """
    # images = Path(__file__).parent.parent / 'assets'
    if evaluate(new_face, Image.open(image), model):
        return image.with_suffix("").name
    return None


def predict(camera_image: Image, model: Model):
    # pool = multiprocessing.Pool()
    predictions = []
    for i in (Path(__file__).parent.parent / 'assets').iterdir():
        # predictions.append(pool.map(check_saved, (camera_image, i, model)))
        predictions.append(check_saved(camera_image, i, model))
    # pool.close()
    # pool.join()
    print(predictions)


def get_image() -> Image:
    """
    Reads user's face from camera, if there's an error throws CameraNotFunctioning error
    :return:
    """
    cam = cv2.VideoCapture(0)
    for i in range(5):
        ret, frame = cam.read()
        if not ret:
            raise CameraNotFunctioning("Check if your camera is working fine!") from None

    cam.release()
    cv2.destroyAllWindows()

    return Image.fromarray(frame)


def extract_face(image) -> np.array:
    """
    Extracts faces from the image
    :param image:
    :return:
    """
    image_array = np.asarray(image)
    detector = MTCNN()
    res = detector.detect_faces(image_array)
    # x2 and y2 as width and height respectively
    if not res:
        raise FaceNotDetected("There has been an error with your face :(") from None
    x1, y1, x2, y2 = res[0]['box']
    # bottom corner
    x2 += x1
    y2 += y2
    face = image_array[y1:y2, x1:x2]
    return np.asarray(Image.fromarray(face).resize((224, 224)))


def evaluate(image1: Image, image2: Image, model: Model, threshold: int = THRESHOLD) -> bool:
    """
    Evaluates whether the given images represent the same person
    :param model:
    :param image1:
    :param image2:
    :param threshold:
    :return:
    """
    faces = [extract_face(image1), extract_face(image2)]
    samples = preprocess_input(np.asarray(faces, 'float32'))
    embeddings = model.predict(samples, batch_size=64)
    score = cosine(embeddings[0], embeddings[1])
    if score <= threshold:
        return True
    return False


if __name__ == '__main__':
    # print(evaluate(Image.open(str(Path(__file__).parent.parent / 'assets' / '1.jpg')), get_image()))
    _model = create_model()
    predict(get_image(), _model)
