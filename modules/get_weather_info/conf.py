from entities.ent_enabled_module import EnabledModule
from entities.ent_chat_keyword import ChatKeyword
from modules.get_weather_info.get_weather_info import get_weather_info

ENABLED_MODULE = EnabledModule(
    class_name=get_weather_info().getStrClassName(),
    custom_json_settings={}
)

""" TODO: Remove chat keywords and use chatterbot yaml (make own files
for each module and then train the bot for this file. :) """

CHAT_KEYWORDS = [
    ChatKeyword(chat_keyword="weather in")
]

# Dependencies of the module
DEPENDENCIES = [
    "weather-api"
]