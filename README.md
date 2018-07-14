# Python_HomeAssistant [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/wsdt/Python_HomeAssistant.svg)](https://github.com/wsdt/Python_HomeAssistant/blob/master/LICENSE) [![Generic badge](https://img.shields.io/badge/Docker-Compatible-blue.svg)](https://shields.io/)

Easy to use home assistant to talk to, get several information, controlling your IoT-devices and the best of all **keeping your data private/locally**. Therefore, the assistant can operate offline except some enabled apis (e.g. Instagram, etc.). Would love to see some reactions (issues, pull-requests, etc.). Please note, that this project is young and has not all featured functionalities. 

## Releases [![GitHub release](https://img.shields.io/github/release/wsdt/Python_HomeAssistant.svg)](https://GitHub.com/wsdt/Python_HomeAssistant/releases/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/wsdt/Python_HomeAssistant/graphs/commit-activity)

Project currently under development, so there are no production-ready releases yet. 

## Contribution [![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

This project is licensed under Apache 2.0, so contributions/pull-requests are welcome. All contributors get listed here. 

**Contributors** [![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/kennethreitz)
- Kevin Riedl ([WSDT](https://github.com/wsdt))

## How to get started
Start main.py to use the full functional home assistant. I recommend that you use Docker, for that I have provided a [Dockerfile](https://github.com/wsdt/Python_HomeAssistant/blob/master/docker/Dockerfile).

### Confidential.py
You will need the CONFIDENTIAL.py file to use this bot. For that I provided a CONFIDENTIAL_Template.py-File
which contains example parameters. Please change all params and then rename the file to "CONFIDENTIAL.py". 

After that you will be able to use the bot in Telegram with all it's features. 

### Docker-Ready
To start the bot without any complications I made a Dockerfile for you guys. Just switch to the subdirectory 'docker' and you will see the Dockerfile. 
1. Build the dockerfile with the CONFIDENTIAL.py-file in the same directory as the Dockerfile. 
``` docker build -t wsdt/homeAssistant . ```
1. Start a new container out of the newly created/built image: 
``` docker run wsdt/homeAssistant ```
1. Verify that the container is running by: 
``` docker ps -a ```


## Python_Chatbot
You might have seen that I published also a quite similar repository called Python_Chatbot [https://github.com/wsdt/Python_chatbot]. The Python_Chatbot repository is only a simple chatbot for your Telegram app, which can conversate with you and has some additional features like some information about your Instagram account, random quotes/pics/questions etc. 

In contrast to that **this** repository aims to be a fully functional home assistant for e.g. your Raspberry Pi. Later this assistant will use voice recognition and will have access to all your IoT-devices by a modular interface. 
