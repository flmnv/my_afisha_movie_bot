class Response:
    def __init__(self, status_code: int, json):
        self.status_code = status_code
        self.json = json
