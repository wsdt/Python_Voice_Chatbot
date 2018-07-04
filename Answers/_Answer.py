from abc import abstractmethod, ABC


# PARENT CLASS

class Answer(ABC):
    @staticmethod
    @abstractmethod
    def getAnswer(bot,update):
        raise NotImplementedError
