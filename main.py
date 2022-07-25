import pandas as pd
import string_manipulation

#overall parameters
csv_file = "test_data.csv"


if __name__ == '__main__':
    df = pd.read_csv(csv_file)
    questions = [string_manipulation.create_questions_from_answers(x) for x in df['Phrase']]
    df['Questions'] = questions
    print(df.loc[:, ['Topic','Questions']])