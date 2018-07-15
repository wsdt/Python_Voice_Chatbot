import sqlite3

""" Manages the dbConnections 
@:param whatToDo -> Is a function which needs a dbCursor as
    parameter. Inside this method the dbOperations are executed.
"""
def doWithDb(whatToDo):
    db = sqlite3.connect('db')
    # Execute provided function with dbCursor
    whatToDo(db.cursor())
    db.commit() # save changes
    db.close()