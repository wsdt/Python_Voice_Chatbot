from starterkit.abstr_answer import abstr_answer
from weather import Weather, Unit

class get_weather_info(abstr_answer):
    def getAnswer(self, userInput):
        return "Welcome to PyChatbot :)"

    def getLocation(self, userInput):
        for chat_keyword in self.getChatKeywords():
            userInput.replace(chat_keyword,'') # remove from input
        return userInput # hopefully only returning state/location