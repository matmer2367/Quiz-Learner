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

def go_through_quiz_shuffled(quiz: quiz_manager.QuizManager):
    quiz.shuffle_current_quiz()
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
    quiz.reset_current_quiz_order()

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

def get_input_number(prompt: str) -> int:
    try:
        num = int(input(prompt))
        return num
    except:
        return -1

def get_input_number_ranged(prompt: str, range_from: int, range_to: int) -> int:
    try:
        num = int(input(prompt))
        if range_from <= num <= range_to:
            return num
    except:
        pass
    return -1

while True:
    os.system("cls")
    show_quizes_list(quiz)
    print(f"")
    print(f"0: read description")
    print(f"1: start quiz")
    print(f"2: Exit")
    print(f"")
    option = get_input_number_ranged(f"Select Option: ", 0, 2)

    if option == -1:
        os.system("cls")
        continue

    if option == 2:
        os.system("cls")
        break

    while True:
        os.system("cls")
        show_quizes_list(quiz)
        quiz_selection = get_input_number_ranged(f"which one?: ", 0, quiz.get_amount_of_quizes())
        if quiz_selection == -1:
            continue
        break


    quiz.current_quiz_selector = quiz_selection

    os.system("cls")
    if option == 0:
        print(f"Name: {quiz.get_current_quiz_name()}")
        input(f"Description:\n{quiz.get_current_quiz_description()}")
        quiz.reset_counters()
    elif option == 1:
        go_through_quiz_shuffled(quiz)
