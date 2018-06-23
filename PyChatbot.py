import os
import Answers

class PyChatbot():
    VERSION = "0.1"
    INPUT_INDICATOR = "[-- "


    def printMenu(self):
        mainMenuOptions = {
            -1: PyChatbot.showError,
            0: PyChatbot.exitChatBot,
            1: PyChatbot.startChatbot,
            2: PyChatbot.openSettings
        }

        print("*************** Chatbot ****************")
        print("Version: "+PyChatbot.VERSION)
        print("\nWelcome to my very first Python Chatbot.\n"
              "Below you will find a small menu which can be navigated by your keypresses (e.g. 1, ..)\n\n")
        print("* (1) Start chatting * (2) Settings * (0) Exit *\n")

        try:
            # Execute corresponding method
            mainMenuOptions.get(int(input(PyChatbot.INPUT_INDICATOR)),-1)(self)
        except ValueError:
            print("\nERROR: Menu only accepts integer values.")
            PyChatbot.exitChatBot(self)

    def showError(self):
        print("\nERROR: An error in "+self.__class__.__name__+" occured, maybe you have selected a non-existing option.")
        PyChatbot.exitChatBot(self)

    def exitChatBot(self):
        print("\n########## Exiting chatbot. ###########")
        exit()

    def startChatbot(self):
        os.system('cls' if os.name=='nt' else 'clear')
        while True:
            print(PyChatbot.getAnswer(self,input(PyChatbot.INPUT_INDICATOR)))

    def getAnswer(self, userInput):
        if "?" in userInput:
            Answers.AnswerQuestion.getAnswer()
        return userInput

    def openSettings(self):
        print("NOTICE: Feature not available (in construction).")
        PyChatbot.exitChatBot(self)








