from time import sleep
from pathlib import Path
from mtcnn.mtcnn import MTCNN
from PIL import Image
from numpy import asarray
import cv2
from scipy.spatial.distance import cosine
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input

THRESHOLD = 0.5


class FaceNotDetected(ValueError):
    pass


def add_face(image: Image):
    max_index = max([int(x.with_suffix("").name) for x in (Path(__file__).parent.parent / 'assets').iterdir()])
    target_path = Path(__file__).parent.parent / 'assets' / f'{max_index + 1}.jpg'
    image.save(str(target_path))


def check_saved(new_face: Image):
    images = Path(__file__).parent.parent / 'assets'
    for i in images.iterdir():
        if evaluate(new_face, Image.open(str(i))):
            return i.with_suffix("").name
    return None


def get_image():
    cam = cv2.VideoCapture(0)
    for i in range(5):
        _, frame = cam.read()

    cam.release()
    cv2.destroyAllWindows()

    return Image.fromarray(frame)


def extract_face(image):
    image_array = asarray(image)
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
    return asarray(Image.fromarray(face).resize((224, 224)))


def evaluate(image1: Image, image2: Image, threshold: int = THRESHOLD):
    faces = [extract_face(image1), extract_face(image2)]
    samples = preprocess_input(asarray(faces, 'float32'))
    model = VGGFace(include_top=False, model='resnet50', input_shape=(224, 224, 3), pooling='avg')
    embeddings = model.predict(samples)
    score = cosine(embeddings[0], embeddings[1])
    if score <= threshold:
        return True
    return False


if __name__ == '__main__':
    # print(evaluate(Image.open(str(Path(__file__).parent.parent / 'assets' / '1.jpg')), get_image()))
    print(check_saved(get_image()))
