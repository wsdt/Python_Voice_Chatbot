from entities.ent_enabled_module import EnabledModule
from entities.ent_chat_keyword import ChatKeyword

ENABLED_MODULE = EnabledModule(
    class_name="get_welcome_msg",
    custom_json_settings="{}"
)

CHAT_KEYWORDS = [
    ChatKeyword(chat_keyword="/start")
]