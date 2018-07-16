#!/usr/bin/python3
import configure
from mgr.mgr_voices import liveSpeech
#import sqlite3
from peewee import *



def main():
    # TODO: remove
    test_sql()


    # Configure confidential before if there is a confidential.py
    configure.config_confidential()

    # Start Voice Recognition
    liveSpeech()

def test_sql():
    print("Making sql now")
    """ Peewee Models (Sqlite3) """
    #db = sqlite3.connect('db')
    db = SqliteDatabase('db.sqlite3') #works

    class Person(Model):
        name = CharField()
        class Meta:
            database = db

    db.connect()
    db.create_tables([Person])

if __name__ == '__main__':
    main()
