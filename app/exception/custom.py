class CustomException(Exception):
    def __init__(self, message: str):
        self.name = message


