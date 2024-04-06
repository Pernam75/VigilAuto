from VigilAuto import logger
from VigilAuto.entity.config_entity import TTSConfig
from pathlib import Path
import requests 

class TTS:
    def __init__(self, config:TTSConfig):
        self.config=config
        if not Path(config.output_folder).exists():
            logger.info(f"Creating output folder: {config.output_folder}")
            Path(config.output_folder).mkdir(parents=True, exist_ok=True)
        
    def synthetize(self, text:str, file_id: str) -> str:
        payload = {
            "model_id": self.config.model_id,
            "text": text
        }
        headers = {
            "xi-api-key": self.config.elevenlab_key,
            "Content-Type": "application/json"
        }

        response = requests.request("POST", self.config.url, json=payload, headers=headers)
        
        output_path = Path(self.config.output_folder) / f"{file_id}_{self.config.file_path}"

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        return output_path

""" LEGACY CODE

from VigilAuto import logger
from VigilAuto.entity.config_entity import TTSConfig
from pathlib import Path
from TTS.api import TTS as TTS_API

class TTS:
    def __init__(self, config: TTSConfig):
        self.config = config
        logger.info(f"Loading TTS model: {config.model_name}")
        self.model = TTS_API(model_name=config.model_name, progress_bar=False)
        logger.info(f"Model loaded.")
        if not Path(config.output_folder).exists():
            logger.info(f"Creating output folder: {config.output_folder}")
            Path(config.output_folder).mkdir(parents=True, exist_ok=True)
            

    def synthetize(self, text_input: str, file_id: str) -> str:
        output_path = Path(self.config.output_folder) / f"{file_id}_{self.config.file_path}"
        logger.info(f"Synthetizing text to audio: {input}")
        self.model.tts_to_file(text=text_input, file_path=output_path)
        return output_path
"""