class Question:
    def __init__(self, question: str, correct_answer: str, topic: str):
        self.question_text = question
        self.correct_answer = correct_answer
        self.question_topic = topic