# ©️ Dan Gazizullin, 2021-2023
# This file is a part of Hikka Userbot
# 🌐 https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

# ©️ Codrago, 2024-2025
# This file is a part of Heroku Userbot
# 🌐 https://github.com/coddrago/Heroku
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html


import logging

from .. import loader, utils
from herokutl.tl.types import Message


logger = logging.getLogger(__name__)


@loader.tds
class StandartMod(loader.Module):
    """Control standart userbot settings"""

    strings = {"name": "Standart"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Text_Of_Ping",
                "<emoji document_id=5920515922505765329>⚡️</emoji> <b>Ping: </b><code>{ping}</code><b> 𝚖𝚜 </b>\n<emoji document_id=5900104897885376843>🕓</emoji><b> Uptime: </b><code>{uptime}</code>",
                lambda: self.strings["configping"],
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "hint",
                None,
                lambda: self.strings["hint"],
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "ping_emoji",
                "🪐",
                lambda: self.strings["ping_emoji"],
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
                "banner_url",
                None,
                lambda: self.strings["banner_url"],
                validator=loader.validators.String(),
            ),
        )

    @loader.command()
    async def ping(self, message: Message):
        """- Find out your userbot ping"""
        start = time.perf_counter_ns()
        message = await utils.answer(message, self.config["ping_emoji"])
        banner = self.config["banner_url"]
        
        if self.config["banner_url"]:
            await utils.answer(
                message,
                self.config["Text_Of_Ping"].format(
                    ping=round((time.perf_counter_ns() - start) / 10**6, 3),
                    uptime=utils.formatted_uptime(),
                    ping_hint=(
                        (self.config["hint"]) if random.choice([0, 0, 1]) == 1 else ""
                    ),
                    hostname=lib_platform.node(),
                    user=getpass.getuser(),
                    prefix=self.get_prefix(),
                    
        ),
                file = banner,
                reply_to=getattr(message, "reply_to_msg_id", None),
            )

        else:
            await utils.answer(
                message,
                self.config["Text_Of_Ping"].format(
                    ping=round((time.perf_counter_ns() - start) / 10**6, 3),
                    uptime=utils.formatted_uptime(),
                    ping_hint=(
                        (self.config["hint"]) if random.choice([0, 0, 1]) == 1 else ""
                    ),
                    hostname=lib_platform.node(),
                    user=getpass.getuser(),
        ),
            )
    
    def _pass_config_to_logger(self):
        logging.getLogger().handlers[0].force_send_all = self.config["force_send_all"]
        logging.getLogger().handlers[0].tg_level = {
            "INFO": 20,
            "WARNING": 30,
            "ERROR": 40,
            "CRITICAL": 50,
        }[self.config["tglog_level"]]
        logging.getLogger().handlers[0].ignore_common = self.config["ignore_common"]

    async def client_ready(self):
        chat, _ = await utils.asset_channel(
            self._client,
            "eye-logs",
            "👀 Your EyeBot logs will appear in this chat",
            silent=True,
            invite_bot=True,
            avatar="https://raw.githubusercontent.com/coddrago/assets/refs/heads/main/heroku/heroku_logs.png",
        )

        self.logchat = int(f"-100{chat.id}")

        logging.getLogger().handlers[0].install_tg_log(self)
        logger.debug("Bot logging installed for %s", self.logchat)

        self._pass_config_to_logger()