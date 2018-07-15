from answers.abstr_answer import abstr_answer


class get_welcome_msg(abstr_answer):
    chat_keywords = ["/start"]

    @staticmethod
    def getAnswer(userInput):
        return "Welcome to PyChatbot :)"


