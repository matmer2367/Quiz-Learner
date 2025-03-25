from .QuizData import QuizData
from . import file_handler

class QuizDataFactory:
    def __init__(self):
        self.path = ""

    def __path_defined(self):
        return self.path != ""

    def set_file_path(self, path: str):
        self.path = path
        try:
            f = open(path)
        except:
            self.path = ""
            print(f"Path {path} is not a real file")

    def load_data(self) -> QuizData:
        if not self.__path_defined:
            print(f"Path of file is not defined yet")
            return
        data = file_handler.loadFile(self.path)
        return QuizData(data)