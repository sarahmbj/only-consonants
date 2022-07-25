class Question:
    def __init__(self, question: str, correct_answer: str):
        self.question_text = question
        self.correct_answer = correct_answer
        self.question_topic = None #TODO add this in later