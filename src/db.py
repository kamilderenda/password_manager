from pathlib import Path
from collections import defaultdict
import hashlib
import json
from typing import Union


class DBControl:
    current_user_id: int = 0

    def __init__(self, file_path: Union[str, Path]):
        self.file_path = Path(file_path)
        self.file_path.touch(exist_ok=True)
        self.data = {}

    def add_password(self, user_id: int, login: str, password: str, website: str) -> None:
        self.data[user_id]['passwords'].append({'website': website, 'login': login, 'password': password})

    def add_user(self, username: str) -> None:
        self.data[self.current_user_id] = {'username': username, 'passwords': []}
        self.current_user_id += 1

    def retrieve_passwords(self, user_id: int) -> list:
        if self.data.get(user_id):
            return [i for i in self.data[user_id]['passwords']]
        return []

    def retrieve_users(self) -> list:
        if self.keys():
            return [i for i in self.data]
        return []

    def delete_password(self, user_id: int, website: str) -> None:
        del_index = [i for i in self.data[user_id]['passwords'] if i['website'] == website]
        if del_index:
            del self.data['passwords'][del_index]

    def delete_user(self, user_id: int):
        ...

    def modify_password(self, user_id: int, website: str, new_password: str):
        ...

    def _get_max_index(self):
        return max(self.data)

    def save(self):
        ...

    def load_data(self):
        ...


if __name__ == "__main__":
    db = DBControl(Path(__file__).parent.parent / 'db.json')
