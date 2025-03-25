from . import QuizDataHandling as quiz_data_handling
import os
from typing import List

class QuizDirectoryManager:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def get_quiz_data_list(self) -> List[quiz_data_handling.QuizData]:
        found_files = os.listdir(self.directory_path)
        quiz_data_factory = quiz_data_handling.QuizDataFactory()
        quiz_data_list = []
        for f_string in found_files:
            quiz_data_factory.set_file_path(f"{self.directory_path}{f_string}")
            quiz_data_list.append(quiz_data_factory.load_data())
        return quiz_data_list