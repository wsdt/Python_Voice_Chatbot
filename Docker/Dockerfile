# Before you build you should have the CONFIDENTIAL.py in your current dir

# Install dependencies
FROM python

RUN pip install chatterbot && \
	pip install InstagramApi && \
	pip install pocketsphinx && \
	pip install pyttsx3 && \
	git clone https://github.com/wsdt/Python_HomeAssistant.git
	
# Copy your secrets into the image	
COPY CONFIDENTIAL.py Python_HomeAssistant/
	
# Collect newest version and then start bot
CMD cd Python_HomeAssistant&&git pull&&python main.py
