#  Copyright (c) Vladislav Filimonov <vladislav.flmnv@yandex.ru>, 2023.
#  Last modified: 09.03.2023, 23:56.

class Response:
    def __init__(self, status_code: int, json):
        self.status_code = status_code
        self.json = json
