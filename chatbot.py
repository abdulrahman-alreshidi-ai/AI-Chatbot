import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ChatBot:

    def __init__(self):

        with open("knowledge.json", "r") as file:
            self.knowledge = json.load(file)

        self.questions = list(self.knowledge.keys())
        self.answers = list(self.knowledge.values())

        self.vectorizer = TfidfVectorizer()

        self.vectors = self.vectorizer.fit_transform(
            self.questions
        )


    def get_response(self, user_input):

        user_vector = self.vectorizer.transform(
            [user_input.lower()]
        )

        similarity = cosine_similarity(
            user_vector,
            self.vectors
        )

        index = similarity.argmax()

        score = similarity[0][index]


        if score < 0.2:
            return "Sorry, I don't understand."


        return self.answers[index]
