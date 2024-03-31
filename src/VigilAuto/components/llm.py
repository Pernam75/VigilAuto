from VigilAuto import logger
from VigilAuto.entity.config_entity import LLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

class LLM:
    def __init__(self, config: LLMConfig):
        self.config = config
        self.chat = ChatGroq(groq_api_key=config.groq_api_key, temperature=config.temperature, model_name=config.model_name)

    def get_response(self, human_prompt: str) -> str:
        prompt = ChatPromptTemplate.from_messages([("system", self.config.system_prompt + f"{self.config.max_tokens_response} tokens."), ("human", human_prompt)])
        chain = prompt | self.chat
        result = chain.invoke({"text": human_prompt})
        return result