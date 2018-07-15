import os
from mgr.mgr_db import doWithDb

# TODO: Import the configuration needs to be done AFTER the smart-learning! So maybe place that also here (otherwise learning is never done)

""" This file configures the assistant by loading the CONFIDENTIAL.py and saving it into
the database. When no CONFIDENTIAL.py is available all settings are kept. For revision:
You need the CONFIDENTIAL.py only on your first startup and then only if you change a huge
amount of your settings quickly. """

def config_confidential():
    # Save confidential settings into db if CONFIDENTIAL.py exists
    if os.path.exists('CONFIDENTIAL.py'):
        # CONFIDENTIAL exists, save all settings to the db
        print("configure: CONFIDENTIAL.py found.\n"
              "If you have started this bot with that file before then I recommend that you rename your CONFIDENTIAL.py to CONFIDENTIAL_backup.py for a better performance.\n"
              "If you have not started this assistant with a valid CONFIDENTIAL.py before, then you did everything right :)")
        # save to db
        doWithDb(save_confidential) #do not call function just give it to doWithDb
    else:
        print("configure: Have not found a CONFIDENTIAL.py. \n"+
              "If you have started this bot with that file before then everything should be fine :).\n"
              "If you have not configured your default settings, then the assistant might not work correctly.")


# Only invoked when confidential.py exists
def save_confidential(dbCursor):
    print("configure: Saving confidential.py.")
    #TODO: use orm e.g. peewee or similar
    #TODO: convert confidential py to db and create tables if they dont exist