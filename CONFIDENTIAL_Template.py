from answers.get_welcome_msg import get_welcome_msg
from answers.random.get_random_fact import get_random_fact
from answers.random.get_random_question import get_random_question
from answers.api.get_instagram_info import get_instagram_info


""" This file is only needed ONCE (when executing the assistant the first time).

 Nevertheless, if you don't delete/rename this file (regardless of making changes), then 
 the whole file is saved into the current database (older settings get overwritten).
 You could use this functionality to quickly overwrite all/a huge amount of the 
 assistants settings. But, keep in mind that you might be able to change all
 params also via voice command (see docu on Github). 
 
 Additionally, if you delete the assistants database (what you can do, he will "learn"
 everything automatically again on the next startup), you might need this file AGAIN to
 configure all settings. So, I strongly recommend you to rename this file to e.g.
 CONFIDENTIAL_backup.py. The CONFIDENTIAL.py and CONFIDENTIAL_backup.py are placed
 in the .gitignore. When renaming it to another name, I suggest you to add the 
 corresponding name into the .gitignore. 
 
 All params are set with example values. The comment above always indicates whether
 a change is OPTIONAL or OBLIGATORY to let the bot working."""

""" ++++++++++++++++++++++ Assistant modules +++++++++++++++++++++++++++++++++++++++ 
No modules are required. If you don't want to use any additional features, then
you can change the following array to an empty one: 
    ENABLED_MODULES = []
    
If you disabled all modules then the assistant can only talk with you (= get_smart_answer). 
By this you can also easily add some modules to your project and place it here into the list. 
The more modules you have enabled the longer a potential answer of the bot might need. 

You can also create modules by your own. Just look into abstr_answer.py for a more detailed
documentation. When you created one you can place the file where you want to, I strongly
recommend the 'answers' package to keep the project structure clean and then just import it
here and place it in the 'ENABLED_MODULES'-array. 

CHANGE:     ++ OPTIONAL ++ [-> by default, the assistant uses all modules]
"""
ENABLED_MODULES = [
    get_welcome_msg,
    get_random_question,
    get_random_fact,
    get_instagram_info
]


""" ++++++++++++++++++++++ Instagram Login Credentials ++++++++++++++++++++++++++++++ 
If you want to use the Instagram Features just add your username and password below. 

CHANGE:     ++ OPTIONAL ++ [-> otherwise you are not able to access the instagram featuers]
"""
INSTAGRAM_API = {
    "USERNAME":"YOUR_USERNAME_HERE",
    "PASSWORD":"YOUR_PASSWORD_HERE"
}

