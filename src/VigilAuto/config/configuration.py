from VigilAuto.constants import *
from VigilAuto.utils.common import read_yaml
from VigilAuto.entity.config_entity import (LLMConfig,
                                            TTSConfig,
                                            STTConfig)
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
            self.secrets = None

    def get_llm_config(self):
        config = self.config.llm
        secrets = self.secrets.llm if self.secrets else None
        return LLMConfig(
            groq_api_key=secrets.groq_api_key if secrets else os.getenv("GROQ_API_KEY"),
            system_prompt=config.system_prompt,
            max_tokens_response=config.max_tokens_response,
            temperature=config.temperature,
            model_name=config.model_name
        )
      
    def get_tts_config(self):
        config = self.config.tts
        secrets = self.secrets.tts if self.secrets else None
        return TTSConfig(
            model_id=config.model_id,
            elevenlab_key=secrets.elevenlab_key if secrets else os.getenv("ELEVENLAB_KEY"),
            url=config.url + config.voice_id,
            output_folder=config.output_folder,
            file_path=config.file_path
        )
    
    def get_stt_config(self):
        config = self.config.stt
        return STTConfig(
            model_name=config.model_name
        )