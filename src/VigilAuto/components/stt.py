from VigilAuto import logger
from VigilAuto.entity.config_entity import STTConfig
import whisper

class STT:
    def __init__(self, config: STTConfig):
        self.config = config
        self.model = whisper.load_model(config.model_name)

    def transcribe(self, audio_path: str) -> str:
        return self.model.transcribe(audio_path)['text']