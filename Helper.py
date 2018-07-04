import sqlite3

""" Converts a dictionary to a list by only adding
the keys of the dict to the list. """
def dict2listByKey(dict):
    list = []
    for key in dict:
        list.append(key)
    return list

""" Manages the dbConnections 
@:param whatToDo -> Is a function which needs a dbCursor as
    parameter. Inside this method the dbOperations are executed.
"""
def doWithDb(whatToDo):
    db = sqlite3.connect('db')
    # Execute provided function with dbCursor
    whatToDo(db.cursor())
    db.commit() #save changes
    db.close()