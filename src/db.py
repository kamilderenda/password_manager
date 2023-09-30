from pathlib import Path
from collections import defaultdict
import hashlib
import json
from typing import Union


class DBControl:
    current_user_id: int = 0

    def __init__(self, file_path: Union[str, Path]):
        self.file_path = Path(file_path)
        '''if self.file_path.exists():
            self.data = self.load_data()
        else:
            self.file_path.touch()
            self.data = {}'''
        self.data = self.load_data()

    def add_password(self, user_id: int, login: str, password: str, website: str) -> None:
        self.data[str(user_id)]['passwords'].append({'website': website, 'login': login, 'password': password})

    def add_user(self, username: str) -> None:
        self.data[str(self.current_user_id)] = {'username': username, 'passwords': []}
        self.current_user_id += 1

    def retrieve_passwords(self, user_id: int) -> list:
        if self.data.get(user_id):
            return [i for i in self.data[user_id]['passwords']]
        return []

    def retrieve_users(self) -> list:
        if self.data.keys():
            return [i for i in self.data]
        return []

    def delete_password(self, user_id: int, website: str) -> None:
        del_index = [x for x, i in enumerate(self.data[user_id]['passwords']) if i['website'] == website]  # lista!!!
        if del_index:
            del self.data[user_id]['passwords'][del_index[0]]

    def delete_user(self, user_id: int):
        if self.data.get(user_id):
            del self.data[user_id]

    def modify_password(self, user_id: int, old_website: str, new_website: str, new_login: str, new_password: str):
        if self.data.get(user_id):
            mod_index = [x for x, i in enumerate(self.data[user_id]['passwords']) if i['website'] == old_website]
            if mod_index:
                self.data[user_id]['passwords'][mod_index[0]] = {'website': new_website,
                                                                 'login': new_login, 'password': new_password}

    # def _get_max_index(self):
    #    return max(self.data)

    def save(self):
        with open(str(self.file_path), 'w') as file:
            json.dump(self.data, file)

    def load_data(self):
        if self.file_path.exists():
            with open(str(self.file_path)) as file:
                data = json.load(file)
            if data:
                DBControl.current_user_id = int(max(data.keys())) + 1
                return data
        return {}


if __name__ == "__main__":
    db = DBControl(Path(__file__).parent.parent / 'db.json')
    # db.modify_password(1, 'fs', 'fdsd', 'gdfgd')
    db.save()
