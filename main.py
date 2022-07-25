import pandas as pd
import re
import random

#overall parameters
csv_file = "test_data.csv"

# String manipulation functions
def leave_only_consonants(lowercased_phrase):
    not_consonants = re.compile(r'[^bcdfghjklmnpqrstvwxyz]')
    only_consonants_phrase = re.sub(not_consonants, "", lowercased_phrase)
    return only_consonants_phrase


def insert_spaces(phrase):
    phrase = list(phrase)
    spaces = list(range(len(phrase)))
    random.shuffle(spaces)

    #truncate to create max spaces
    max_spaces = int(len(phrase)/2)
    spaces = spaces[0:max_spaces]

    #loop through space indexes and randomly delete some (to vary number of spaces)
    selected_spaces = []
    for i in range(len(spaces)-1):
        coin_flip = random.randrange(2)
        if coin_flip == True:
            selected_spaces.append(spaces[i])

    #add the spaces to the phrase
    for i in selected_spaces:
            phrase[i] = phrase[i] + ' '
    phrase_with_spaces = ''.join(phrase)

    #find and remove consecutive spaces
    multiple_spaces = re.compile(r'\s\s+')
    phrase_with_spaces = re.sub(multiple_spaces, " ", phrase_with_spaces)
    return phrase_with_spaces


def create_questions_from_answers(answer):
        question = answer.lower()
        question = leave_only_consonants(question)
        question = insert_spaces(question)
        return(question)

#TODO: create test file
# test_string = "The White Album"
# test_string = leave_only_consonants(test_string)
# test_string =insert_spaces(test_string)
# print(test_string)

#main method
df = pd.read_csv(csv_file)
questions = [create_questions_from_answers(x) for x in df['Phrase']]
df['Questions'] = questions
print(df)
