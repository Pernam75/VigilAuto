from VigilAuto import logger
from VigilAuto.entity.config_entity import TTSConfig
from pathlib import Path
from elevenlabs.client import ElevenLabs
from elevenlabs import save # TODO stream method is also available
class TTS:
    def __init__(self, config:TTSConfig):
        self.config=config
        if not Path(config.output_folder).exists():
            logger.info(f"Creating output folder: {config.output_folder}")
            Path(config.output_folder).mkdir(parents=True, exist_ok=True)
        
    def synthetize(self, text:str, file_id: str) -> str:
        
        output_path = Path(self.config.output_folder) / f"{file_id}_{self.config.file_path}"
        client = ElevenLabs(
            api_key=self.config.elevenlab_key
        )
        audio = client.generate(
            text=text,
            voice=self.config.voice_id,
            model=self.config.model_id,
        )
        try:
            save(audio, output_path)
        except Exception as e:
            print(f"Error when saving the output file: {e}")
            return None
        return output_path
