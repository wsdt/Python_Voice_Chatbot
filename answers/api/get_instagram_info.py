from answers.abstr_answer import abstr_answer
from InstagramAPI import InstagramAPI
from Helper import dict2listByKey


# Uses Instagram api to do sth
class get_instagram_info(abstr_answer):
    # TODO REMOVE AND REPLACE WITH DB
    InstagramAPI = {
        "USERNAME":"TEST",
        "PASSWORD":"TEST"
    }


    # Prepare instagram api
    igApi = None

    @staticmethod
    def getAnswer(userInput):
        # Login in Ig when api is not set yet (here, so we only login if user wants to access ig Api.
        if get_instagram_info.igApi is None:
            get_instagram_info.igLogin()

        # Evaluate whether we can access the api or not
        if get_instagram_info.igApi.isLoggedIn:
            print("GetInstagramAnswer: Logged in successfully.")
            return get_instagram_info.prepareAnswer(userInput) # has to be before, so answer can get updated

        else:
            print("GetInstagramAnswer: Could not log in into Instagram account. If you have changed your CONFIDENTIAL.py, then restart your bot.")
            return "Could not login into Instagram."


    @staticmethod
    def igLogin():
        get_instagram_info.igApi = InstagramAPI(get_instagram_info.INSTAGRAM_API["USERNAME"], get_instagram_info.INSTAGRAM_API["PASSWORD"])
        get_instagram_info.igApi.login()


    # Craft reply btns and execute command if one is found.
    @staticmethod
    def prepareAnswer(userInput):
        for strCommand,commandMethod in get_instagram_info.chat_commands.items():
            if strCommand == userInput:
                # User executed a command, so save/output now the elaborated information
                return commandMethod()

    @staticmethod
    def getFollowers():
        """ Returns total count of followers of user. """
        followers = []
        next_max_id = True
        while next_max_id:
            # first iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = get_instagram_info.igApi.getUserFollowers(get_instagram_info.igApi.username_id, maxid=next_max_id)
            followers.extend(get_instagram_info.igApi.LastJson.get('users', []))
            next_max_id = get_instagram_info.igApi.LastJson.get('next_max_id', '')
        return "You have currently "+str(len(followers))+" Followers on Instagram."

    @staticmethod
    def getFollowings():
        # Returns total count of followings of user
        get_instagram_info.igApi.getUsernameInfo(get_instagram_info.INSTAGRAM_API["USERNAME"])

        following = []
        next_max_id = True
        while next_max_id:
            # First iteration hack
            if next_max_id is True:
                next_max_id = ''

            _ = get_instagram_info.igApi.getUserFollowings(get_instagram_info.INSTAGRAM_API["USERNAME"], maxid=next_max_id)
            following.extend(get_instagram_info.igApi.LastJson.get('users', []))
            next_max_id = get_instagram_info.igApi.LastJson.get('next_max_id', '')

        # Filter by primary key
        unique_following = {
            f['pk']:f
            for f in following
        }

        return "You follow currently "+str(len(unique_following))+" people. (number [maybe] currently not accurate)"


    # MEMBERS -------------------------------------------------------------------------
    # TODO: Migrate to speakable command
    chat_commands = {
        "/getIgFollowers":getFollowers.__func__,
        "/getIgFollowings":getFollowings.__func__
    }
    chat_keywords = ["instagram","ig"]+dict2listByKey(chat_commands) # Add also chat_commands (without methods) so they have an impact
    answer_text = "What do you want to do/know?" # by default, but might get changed (except for instagram, ig)

