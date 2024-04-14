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
