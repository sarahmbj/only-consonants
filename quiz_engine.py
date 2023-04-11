import re
class QuizEngine:

    def __init__(self, question_bank):
        self.score = 0

        self.topics = question_bank.topics
        self.topics_unplayed = self.topics
        self.topics_played = []

        self.current_round_number = 0
        self.current_round_topic = None
        self.current_round_question_list = None
        self.current_round_questions_played = 0

        self.question_no = 0
        self.current_question = None
        
        # self.total_rounds = 3 #Allow player to set this? Or always have 3?

    def start_new_round(self):
        self.current_round_number += 1
        self.current_round_questions_played = 0
        selected_topic = self.topics_unplayed.pop()
        self.current_round_topic = selected_topic.topic_name
        self.current_round_question_list = selected_topic.questions

        print(f"\n\n**** Starting Round {self.current_round_number} ****"
        f"\n Topic: {self.current_round_topic}")
        
    def quiz_has_more_rounds(self):
        if len(self.topics_unplayed) > 0:
            return True
        else:
            return False
    
    def round_has_more_questions(self):
        """To check if the current round has more questions"""
        
        return self.current_round_questions_played < len(self.current_round_question_list)


    def next_question(self):
        """Get the next question by incrementing the question number"""
        
        self.current_question = self.current_round_question_list[self.current_round_questions_played]
        self.question_no += 1
        self.current_round_questions_played += 1
        q_text = self.current_question.question_text
        q_topic = self.current_question.question_topic
        return f"Topic: {q_topic} \n Q.{self.question_no}: {q_text}"

    def ask_question(self):
        input("Press enter for next question \n")
        print(self.next_question())
        answer = input('Answer: ')
        if self.check_answer(answer)[0] == True:
            print("Correct!")
        else:
            print(f"Sorry, that's not right. Correct answer: {self.current_question.correct_answer}")
            

    def check_answer(self, user_answer):
        """Check the user's answer against the correct answer and maintain the score"""
        #TODO: strip punctuation when validating answers
        only_alpha = re.compile(r'[^a-z\s]')

        correct_answer = self.current_question.correct_answer
        correct_answer_cleaned = correct_answer.lower()
        correct_answer_cleaned = re.sub(only_alpha, "", correct_answer_cleaned)

        user_answer_cleaned = user_answer.lower()
        user_answer_cleaned = re.sub(only_alpha, "", user_answer_cleaned)

        if user_answer_cleaned == correct_answer_cleaned:
            self.score += 1
            return [True, self.current_question.correct_answer]
        else:
            return [False, self.current_question.correct_answer]


    def get_score(self):
        """Get the number of correct answers, wrong answers, and score percentage."""
        
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.total * 100)
        return (self.score, wrong, score_percent)

    def explain_rules(self):
        """Give the player an explanation of how to play the game"""

        print("In this game, you will get shown some text with all the vowels removed, and spaces inserted randomly." 
            "\n Your job is to type in the original phrase as quickly as possible."
            "\n To help you, you will also see the topic of the original phrase."
            "\n When you type your answer, you don't need to worry about punctuation, or getting lowercase/uppercase correct"
            "\n but you do need to get the spelling correct for the game to recognise your answer.")

        input('Press enter to continue \n')

    def end_quiz(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_no}")

    def run_quiz(self):
        print(f"Welcome to Only Consonants. \n")
        show_rules = input('Press enter to get the first question. Or, press any other key to see the rules.')
        if show_rules != "":
            self.explain_rules()
            input('Press enter to start the first round.')

        while self.quiz_has_more_rounds() == True:
            self.start_new_round()
        
            while self.round_has_more_questions() == True:
                self.ask_question()

        self.end_quiz()


#TODO: add ability to select topic at start of game? or ability to skip selected topic?