# Before you build you should have the CONFIDENTIAL.py in your current dir

# Install dependencies
FROM python

RUN pip install chatterbot && python -m pip install python-telegram-bot && \
	pip install InstagramApi && \ 
	git clone https://github.com/wsdt/python_telegram_chatbot.git
	
# Copy your secrets into the image	
COPY CONFIDENTIAL.py python_telegram_chatbot/
	
# Collect newest version and then start bot
CMD cd python_telegram_chatbot&&git pull&&python main.py
