# Before you build you should have the CONFIDENTIAL.py in your current dir

# Install dependencies
FROM python:3
MAINTAINER Kevin Riedl (WSDT) <kevin.riedl.privat@gmail.com>

RUN python -m pip install --upgrade pip setuptools wheel && apt-get update && \
	apt-get install -y build-essential swig git libpulse-dev libasound2-dev espeak && \
	pip install --upgrade pocketsphinx && \
	pip install chatterbot && \
	pip install pyttsx3 && \
	pip install peewee && \
	git clone https://github.com/wsdt/Python_Voice_Chatbot.git && \
	cd Python_Voice_Chatbot&&python setup.py


# Collect newest version and then start bot
CMD cd Python_Voice_Chatbot&&git pull&&python main.py

