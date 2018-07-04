from Answers._Answer import Answer
from InstagramAPI import InstagramAPI
from CONFIDENTIAL import INSTAGRAM_API, AUTHORIZED_USER
import telegram
from Helper import dict2listByKey

# Prepare instagram api
igApi = None



# Uses Instagram api to do sth
class GetInstagramAnswer(Answer):
    @staticmethod
    def getAnswer(bot,update):
        # Login in Ig when api is not set yet (here, so we only login if user wants to access ig Api.
        if igApi is None:
            GetInstagramAnswer.igLogin()

        reply_btns = [GetInstagramAnswer.prepareAnswer(update.message.text)] # has to be before, so answer can get updated
        bot.send_message(chat_id=AUTHORIZED_USER,text=GetInstagramAnswer.answer_text,
                                     reply_markup=telegram.ReplyKeyboardMarkup(reply_btns))

    @staticmethod
    def igLogin():
        igApi = InstagramAPI(INSTAGRAM_API["USERNAME"], INSTAGRAM_API["PASSWORD"])
        igApi.login()

    # Craft reply btns and execute command if one is found.
    @staticmethod
    def prepareAnswer(userInput):
        keyboardBtns = []
        for strCommand,commandMethod in GetInstagramAnswer.chat_commands.items():
            keyboardBtns.append(telegram.KeyboardButton(strCommand))

            if strCommand == userInput:
                # User executed a command, so save/output now the elaborated information
                GetInstagramAnswer.answer_text = commandMethod()

        return keyboardBtns

    @staticmethod
    def getFollowers():
        """ Returns total count of followers of user. """
        followers = []
        next_max_id = True
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = igApi.getUserFollowers(igApi.username_id, maxid=next_max_id)
            followers.extend(igApi.LastJson.get('users',[]))
            next_max_id = igApi.LastJson.get('next_max_id','')
        return "You have currently "+str(len(followers))+" Followers on Instagram."

    @staticmethod
    def getFollowings():
        # Returns total count of followings of user
        igApi.getUsernameInfo(INSTAGRAM_API["USERNAME"])

        following = []
        next_max_id = True
        while next_max_id:
            # First iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = igApi.getUserFollowings(INSTAGRAM_API["USERNAME"], maxid=next_max_id)
            following.extend(igApi.LastJson.get('users', []))
            next_max_id = igApi.LastJson.get('next_max_id','')

        # Filter by primary key
        unique_following = {
            f['pk']:f
            for f in following
        }

        return "You follow currently "+str(len(unique_following))+" people. (number [maybe] currently not accurate)"


    # MEMBERS -------------------------------------------------------------------------
    chat_commands = {
        "/getIgFollowers":getFollowers.__func__,
        "/getIgFollowings":getFollowings.__func__
    }
    chat_keywords = ["instagram","ig"]+dict2listByKey(chat_commands) # Add also chat_commands (without methods) so they have an impact
    answer_text = "What do you want to do/know?" # by default, but might get changed (except for instagram, ig)

