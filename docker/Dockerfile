# Before you build you should have a dir 'python_telegram_bot' with the CONFIDENTIAL.py included

FROM python
RUN pip install chatterbot&&python -m pip install python-telegram-bot

COPY python_telegram_chatbot /python_telegram_bot

CMD cd python_telegram_chatbot && \
	git clone https://github.com/wsdt/python_telegram_chatbot.git && \
	cp -a ./python_telegram_chatbot/. /python_telegram_chatbot/ && \
	rm -rf ./python_telegram_chatbot && \
	python main.py