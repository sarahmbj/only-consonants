import pandas as pd

import string_manipulation
from question_model import Question
from quiz_engine import QuizEngine

# Reference code
# https://www.freecodecamp.org/news/how-to-create-a-gui-quiz-application-using-tkinter-and-open-trivia-db/

#overall parameters
question_file = "test_data.csv"


if __name__ == '__main__':

    question_df = pd.read_csv(question_file)
    questions = [string_manipulation.create_questions_from_answers(x) for x in question_df['Phrase']]
    question_df['Question'] = questions
    # print(question_df.loc[:, ['Topic','Question']])
    #TODO: might want to save questions to a file?

    question_bank = []
    for i in list(question_df.index.values):
        question_text = question_df['Question'].iloc[i]
        correct_answer = question_df['Phrase'].iloc[i]
        new_question = Question(question_text, correct_answer)
        question_bank.append(new_question)

    quiz = QuizEngine(question_bank)

    quiz.run_quiz()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")
#TODO: add something around timing to the final results

