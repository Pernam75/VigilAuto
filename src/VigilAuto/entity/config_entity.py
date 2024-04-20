from dataclasses import dataclass

@dataclass(frozen=True)
class LLMConfig:
    groq_api_key: str
    system_prompt: str
    max_tokens_response: int
    temperature: float
    model_name: str

@dataclass(frozen=True)
class TTSConfig:
    model_id: str
    elevenlab_key: str
    voice_id: str
    output_folder: str
    file_path: str

@dataclass(frozen=True)
class STTConfig:
    model_name: str
