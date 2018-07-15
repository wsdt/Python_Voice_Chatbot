from abc import abstractmethod, ABC


""" PARENT CLASS = MODULE layout 

- How to create a new module?
Each module should/has to extend from abstr_answer, therefore must
implement 'getAnswer()' and needs the class member 'chat_keywords'.

The 'chat_keywords' is an array, which contains keywords. By placing
several keywords there you can decide when your getAnswer() method 
get's invoked. 

So if the userInput contains at least one of your keywords your 
method get's invoked. What you do with the userInput or what you
are answering in general in your method is completely independent
from other modules. Here you see a very simple example module:  

class get_test_msg(abstr_answer):
    chat_keywords = ["test","tst"]

    @staticmethod
    def getAnswer(userInput):
        # Do sth with the userInput, do sth specific or just return
        # a static string. 
        return "Thanks for testing me. You wrote -> "+str(userInput)

"""

class abstr_answer(ABC):
    @staticmethod
    @abstractmethod
    def getAnswer(userInput):
        raise NotImplementedError
