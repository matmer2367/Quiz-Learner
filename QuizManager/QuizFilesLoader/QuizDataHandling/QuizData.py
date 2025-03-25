from typing import List
import random

class QuizData:
    def __init__(self, data: dict):
        self.data = data
        self.default_question_array_order = self.get_questions_list().copy()

    def __str__(self):
        return self.data.__str__()

    def shuffle_data(self):
        random.shuffle(self.get_questions_list())

    def reset_data_order(self):
        self.data["questions"] = self.default_question_array_order.copy()

    def get_name(self) -> str:
        return self.data["name"]

    def get_description(self) -> str:
        return self.data["description"]

    def get_questions_list(self) -> List[List[str]]:
        return self.data["questions"]

    def questions_count(self) -> int:
        return len(self.get_questions_list())

    def get_questions_string(self, index: int) -> str:
        if index >= self.questions_count() or index < 0:
            print("index not valid")
            return ""
        return self.get_questions_list()[index][0]

    def get_answer_string(self, index: int) -> str:
        if index >= self.questions_count() or index < 0:
            print("index not valid")
            return ""
        return self.get_questions_list()[index][1]