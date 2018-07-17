from starterkit.abstr_answer import abstr_answer
import random


class get_random_question(abstr_answer):
    def getAnswer(self, userInput):
        return self.db_loadCustom_json_settings()["random_questions"][random.randint(0, len(get_random_question.questions) - 1)]

