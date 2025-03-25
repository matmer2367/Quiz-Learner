import QuizFilesLoader as qfl

qdp = qfl.QuizDirectoryManager("./quizes/")
quiz_list = qdp.get_quiz_data_list()
print(quiz_list[0])