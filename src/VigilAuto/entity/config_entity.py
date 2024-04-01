from dataclasses import dataclass

@dataclass(frozen=True)
class LLMConfig:
    groq_api_key: str
    system_prompt: str
    max_tokens_response: int
    temperature: float
    model_name: str

@dataclass(frozen=True)
class STTConfig:
    model_name: str