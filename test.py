from VigilAuto.config.configuration import ConfigurationManager
from VigilAuto.components.llm import LLM
from VigilAuto.components.stt import STT
from VigilAuto import logger

def test_llm():
    config_manager = ConfigurationManager()
    llm_config = config_manager.get_llm_config()
    llm = LLM(config=llm_config)
    api_response = llm.get_response("Ceci est un test réponds uniquement par le mot 'reçu' si tu fonctionnes bien")
    print(api_response)
    assert api_response is not None
    assert type(api_response.content) == str

def test_stt():
    config_manager = ConfigurationManager()
    stt_config = config_manager.get_stt_config()
    stt = STT(config=stt_config)
    transcription = stt.transcribe("test_audio.mp3")
    assert transcription is not None
    assert type(transcription) == str
    assert transcription.lower().__contains__("test")
