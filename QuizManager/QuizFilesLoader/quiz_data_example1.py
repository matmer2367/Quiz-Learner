import QuizDataHandling as quiz_data

quiz_data_loader = quiz_data.QuizDataFactory()
quiz_data_loader.set_file_path("./test.yaml")
data1 = quiz_data_loader.load_data()

print(data1.get_questions_string(0))
print(data1.get_answer_string(1))
