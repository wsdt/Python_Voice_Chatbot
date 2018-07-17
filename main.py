#!/usr/bin/python3
from mgr.mgr_voices import liveSpeech
from peewee import *
from mgr.mgr_db import *



def main():
    # Start Voice Recognition
    liveSpeech()

if __name__ == '__main__':
    main()
