import json
from pathlib import Path


class ConfigManager:

    CONFIG_FILE = Path(
        "config.json"
    )

    @staticmethod
    def load():

        if not ConfigManager.CONFIG_FILE.exists():

            default_config = {

                "nickname": "",

                "uuid": "",

                "access_token": "",

                "ram": "4G",

                "accounts": []
            }

            ConfigManager.save(
                default_config
            )

            return default_config

        with open(
            ConfigManager.CONFIG_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    @staticmethod
    def save(config):

        with open(
            ConfigManager.CONFIG_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(

                config,

                file,

                indent=4,

                ensure_ascii=False
            )