from answers.abstr_answer import Answer


class GetWelcomeMsg(Answer):
    chat_keywords = ["/start"]

    @staticmethod
    def getAnswer(userInput):
        return "Welcome to PyChatbot :)"


