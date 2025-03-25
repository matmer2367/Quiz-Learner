from . import QuizFilesLoader as quiz_file_loader
from typing import List

class QuizManager:
    def __init__(self, quiz_data_list: List[quiz_file_loader.QuizData]):
        self.quiz_data_list = quiz_data_list
        self.current_quiz_selector = 0
        self.current_question_selector = 0

    def get_amount_of_quizes(self) -> int:
        return len(self.quiz_data_list)

    def first_quiz_is_reached(self) -> bool:
        return self.current_quiz_selector == 0

    def last_quiz_is_reached(self) -> bool:
        return self.current_quiz_selector == self.get_amount_of_quizes()-1

    def go_next_quiz(self):
        self.current_quiz_selector += 1
        if self.current_quiz_selector >= self.get_amount_of_quizes():
            self.current_quiz_selector = self.get_amount_of_quizes()-1

    def reset_counters(self):
        self.reset_question_counter()
        self.reset_quiz_counter()

    def reset_question_counter(self):
        self.current_question_selector = 0

    def reset_quiz_counter(self):
        self.current_quiz_selector = 0

    def go_previous_quiz(self):
        self.current_quiz_selector -= 1
        if self.current_quiz_selector < 0:
            self.current_quiz_selector = 0

    def __get_quiz_data(self):
        return self.quiz_data_list[self.current_quiz_selector]

    def get_amount_of_questions_current_quiz(self) -> int:
        return self.__get_quiz_data().questions_count()

    def get_questions_left(self) -> int:
        return self.get_amount_of_questions_current_quiz() - (self.current_question_selector+1)

    def last_question_reached(self) -> bool:
        return self.current_question_selector == self.get_amount_of_questions_current_quiz()-1

    def go_next_question(self):
        self.current_question_selector += 1
        if self.current_question_selector >= self.get_amount_of_questions_current_quiz():
            self.current_question_selector = self.get_amount_of_questions_current_quiz()-1

    def shuffle_current_quiz(self):
        self.__get_quiz_data().shuffle_data()

    def reset_current_quiz_order(self):
        self.__get_quiz_data().reset_data_order()

    def get_current_question(self) -> str:
        return self.__get_quiz_data().get_questions_string(self.current_question_selector)

    def get_current_answer(self) -> str:
        return self.__get_quiz_data().get_answer_string(self.current_question_selector)

    def get_current_quiz_name(self) -> str:
        return self.__get_quiz_data().get_name()

    def get_current_quiz_description(self) -> str:
        return self.__get_quiz_data().get_description()