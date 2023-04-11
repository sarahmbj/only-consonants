from question_model import QuestionBank
from quiz_engine import QuizEngine

#overall parameters
question_file = "test_data.csv"


if __name__ == '__main__':
    question_bank = QuestionBank(question_file)
    
    quiz = QuizEngine(question_bank)

    quiz.run_quiz()

# #TODO: add something around timing to the final results