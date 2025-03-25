from . import QuizFilesLoader as quiz_file_loader
from .QuizManager import QuizManager

class QuizManagerFactory:
    def __init__(self):
        self.directory = ""

    def __path_defined(self):
        return self.directory != ""

    def set_directory_path(self, directory_path: str):
        self.directory = directory_path

    def create_quiz_manager(self) -> QuizManager:
        if not self.__path_defined:
            print(f"Path of file is not defined yet")
            return
        quizes = quiz_file_loader.QuizDirectoryManager(self.directory)
        return QuizManager(quizes.get_quiz_data_list())