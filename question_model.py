import pandas as pd
from string_manipulation import create_question_from_answer


class QuestionBank:
    def __init__(self, question_file):
        self.question_df = pd.read_csv(question_file)
        self.topics = self.create_topics()

    def get_question_df(self):
        print(self.question_df)

    def create_topics(self):
        topics = []
        for topic in self.topic_names:
            topic_phrases = self.question_df.loc[self.question_df['Topic'] == topic]
            topic_phrases = topic_phrases['Phrase'].tolist()
            topics.append(self.Topic(topic, topic_phrases))
        return topics

    class Topic:
        def __init__(self, topic_name, topic_phrases):
            self.topic_name = topic_name
            self.topic_phrases = topic_phrases
            self.no_questions = 0
            self.questions = []
            self.create_questions()
            
        def get_topic_name(self):
            print(self.topic_name)

        def create_questions(self):
            for phrase in self.topic_phrases:
                correct_answer = phrase
                question_text = create_question_from_answer(correct_answer)
                question_topic = self.topic_name
                self.questions.append(self.Question(question_text, correct_answer, question_topic))
                self.no_questions += 1

        class Question:
            def __init__(self, question: str, correct_answer: str, topic: str):
                self.question_text = question
                self.correct_answer = correct_answer
                self.question_topic = topic