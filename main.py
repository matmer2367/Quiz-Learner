import QuizManager as quiz_manager
import os

q_factory = quiz_manager.QuizManagerFactory()
q_factory.set_directory_path("./quizes/")
quiz = q_factory.create_quiz_manager()

def go_through_quiz(quiz: quiz_manager.QuizManager):
    print(f"Current quiz: {quiz.get_current_quiz_name()}")

    while True:
        print(f"Question Nr. {quiz.current_question_selector+1}:")
        print(f"_____________________________________________ Questions left: {quiz.get_questions_left()}")
        input(f"{quiz.get_current_question()}\n")
        print(f"{quiz.get_current_answer()}")
        input(f"---------------------------------------------")
        if quiz.last_question_reached():
            break
        quiz.go_next_question()



#go_through_quiz(quiz)

def show_quizes_list(quiz: quiz_manager.QuizManager):
    print(f"We have {quiz.get_amount_of_quizes()} quizes totally")

    while True:
        name = quiz.get_current_quiz_name()
        print(f"{quiz.current_quiz_selector}: {name}")
        if quiz.last_quiz_is_reached():
            break
        quiz.go_next_quiz()
    quiz.reset_quiz_counter()

while True:
    os.system("cls")
    show_quizes_list(quiz)
    print(f"\n0: read description")
    print(f"1: start quiz\n")
    option = int(input(f"Select Option: "))

    if option == 0:
        os.system("cls")
        show_quizes_list(quiz)
        description_read = int(input(f"which one?: "))

        quiz.current_quiz_selector = description_read

        os.system("cls")
        print(f"Name: {quiz.get_current_quiz_name()}")
        input(f"Description:\n{quiz.get_current_quiz_description()}")