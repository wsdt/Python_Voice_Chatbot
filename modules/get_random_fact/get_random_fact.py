import random
from starterkit.abstr_answer import abstr_answer

class get_random_fact(abstr_answer):
    def getAnswer(self, userInput):
        return get_random_fact.facts[random.randint(0, len(get_random_fact.facts) - 1)]

