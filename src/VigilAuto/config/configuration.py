from VigilAuto.constants import *
from VigilAuto.utils.common import read_yaml
from VigilAuto.entity.config_entity import (LLMConfig)
import os

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        secrets_filepath = SECRETS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        try:
            self.secrets = read_yaml(secrets_filepath)
        except FileNotFoundError:
            self.secrets.groq_api_key = os.environ.get("GROQ_API_KEY")

    def get_llm_config(self):
        config = self.config.llm
        secrets = self.secrets.llm
        return LLMConfig(
            groq_api_key=secrets.groq_api_key,
            system_prompt=config.system_prompt,
            max_tokens_response=config.max_tokens_response,
            temperature=config.temperature,
            model_name=config.model_name
        )