import re
class QuizEngine:

    def __init__(self, questions):
        self.score = 0

        self.question_no = 0
        self.questions = questions
        self.current_question = None

        self.current_round_number = 0
        self.total_rounds = 3 #Allow player to set this? Or always have 3?

        self.current_round_topic = None
        self.topics = self.get_topics()
        self.topics_unplayed = self.topics
        self.topics_played = []


    def get_topics(self):
        topics = set()
        for question in self.questions:
            topics.add(question.question_topic)
        return topics

   
    def has_more_questions(self):
        """To check if the quiz has more questions"""
        
        return self.question_no < len(self.questions)


    def next_question(self):
        """Get the next question by incrementing the question number"""
        
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        q_topic = self.current_question.question_topic
        return f"Topic: {q_topic} \n Q.{self.question_no}: {q_text}"


    def check_answer(self, user_answer):
        """Check the user's answer against the correct answer and maintain the score"""

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
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)

    def explain_rules(self):
        """Give the player an explanation of how to play the game"""

        print("In this game, you will get shown some text with all the vowels removed, and spaces inserted randomly." 
            "\n Your job is to type in the original phrase as quickly as possible."
            "\n To help you, you will also see the topic of the original phrase."
            "\n When you type your answer, you don't need to worry about punctuation, or getting lowercase/uppercase correct"
            "\n but you do need to get the spelling correct for the game to recognise your answer.")

        input('Press enter to continue \n')


    def run_quiz(self):
        print(f"Welcome to Only Consonants. \n")
        show_rules = input('Press enter to get the first question. Or, type anything else to see the rules.')
        if show_rules != "":
            self.explain_rules()
            input('Press enter to get the first question.')
        
        while self.has_more_questions() == True:
            print(self.next_question())
            answer = input('Answer: ')
            if self.check_answer(answer)[0] == True:
                print("Correct!")
            else:
                print(f"Sorry, that's not right. Correct answer: {self.current_question.correct_answer}")
            input("Press enter for next question \n")


    def next_round(self):
        self.current_round_number +=1
        self.current_round_topic
        #TODO: finish this! split into rounds by topic


#TODO: add ability to select topic at start of game?#TODO: add ability to select topic at start of game? or ability to skip selected topic?
