from question_model import QuestionBank
from quiz_engine import QuizEngine

#overall parameters
question_file = "test_data.csv"


if __name__ == '__main__':
    question_bank = QuestionBank(question_file)
    print(question_bank.get_question_df())
    print(question_bank.get_topic_names())
    
    quiz = QuizEngine(question_bank)

    quiz.run_quiz()

# #TODO: add something around timing to the final results