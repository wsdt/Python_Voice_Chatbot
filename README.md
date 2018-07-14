# Python_HomeAssistant

Start main.py to use the full functional chatbot in your Telegram app. (Later this repository will remove the Telegram functionality)

## Confidential.py
You will need the CONFIDENTIAL.py file to use this bot. For that I provided a CONFIDENTIAL_Template.py-File
which contains example parameters. Please change all params and then rename the file to "CONFIDENTIAL.py". 

After that you will be able to use the bot in Telegram with all it's features. 

## Docker-Ready
To start the bot without any complications I made a Dockerfile for you guys. Just switch to the subdirectory 'docker' and you will see the Dockerfile. 
1. Build the dockerfile: 
``` docker build -t wsdt/homeAssistant . ```
1. Start a new container out of the newly created/built image: 
``` docker run wsdt/homeAssistant ```
1. Verify that the container is running by: 
``` docker ps -a ```


## Python_Chatbot
You might have seen that I published also a quite similar repository called Python_Chatbot [https://github.com/wsdt/Python_chatbot]. The Python_Chatbot repository is only a simple chatbot for your Telegram app, which can conversate with you and has some additional features like some information about your Instagram account, random quotes/pics/questions etc. 

In contrast to that **this** repository aims to be a fully functional home assistant for e.g. your Raspberry Pi. Later this assistant will use voice recognition and will have access to all your IoT-devices by a modular interface. 
