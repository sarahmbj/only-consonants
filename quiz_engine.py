class QuizEngine:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None
        self.current_round_number = 0
        self.current_round_topic = None
        self.topics = self.get_topics()


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
        #TODO: strip punctuation when validating answers

        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return [True, correct_answer]
        else:
            return [False, correct_answer]


    def get_score(self):
        """Get the number of correct answers, wrong answers, and score percentage."""
        
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)


    def run_quiz(self):
        print(f"Welcome to Only Consonants. Press enter to get the first question.")
        print(f'Available topics: {self.topics}')
        input('')
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


#TODO: add ability to select topic at start of game?