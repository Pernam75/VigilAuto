from VigilAuto import logger
from VigilAuto.entity.config_entity import LLMConfig
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
class LLM:
    def __init__(self, config: LLMConfig):
        self.config = config
        self.chat = ChatGroq(groq_api_key=config.groq_api_key, temperature=config.temperature, model_name=config.model_name)

    def get_response(self, human_prompt: str) -> str:
        prompt = ChatPromptTemplate.from_messages([("system", self.config.system_prompt + f"{self.config.max_tokens_response} tokens."), ("human", human_prompt)])
        chain = prompt | self.chat
        result = chain.invoke({"text": human_prompt})
        return result

class LLMChat:
    def __init__(self, config: LLMConfig, alcool: float):
        self.alcool = alcool
        self.template = """
        Tu es un assistant vocal de conduite. Grâce à une caméra intégrée dans la voiture, le taux d'alcoolémie du conducteur a été mesuré.
        Sache qu'un verre standard d'alccol équivault à 0 point 2 gramme par litre de sang. Si le taux est supérieur à 0 point 5 gramme par litre de sang, tu dois conseiller au conducteur de ne pas conduire. 
        Ne sois pas trop directif ton rôle est de conseiller et non de commander.
        Si le conducteur est en état d'ébriété, tu dois lui proposer de lui commander un taxi ou un VTC.
        Si le conducteur est sobre, tu peux lui donner des conseils sur la conduite ou lui donner des informations sur la route.
        Tu répondras toujours en langue française.
        Reste concis très concis dans tes réponses (maximum 2 phrases)
        Conversation actuelle:
        {history}
        Utilisateur: {input}
        Assistant Vocal:"""
        self.config = config
        self.llm = ChatGroq(groq_api_key=self.config.groq_api_key, model=self.config.model_name, temperature=self.config.temperature)
        self.conversation = ConversationChain(
            prompt=PromptTemplate(input_variables=["history", "input"], template=self.template),
            llm=self.llm,
            verbose=False,
            memory=ConversationBufferMemory(ai_prefix="Assistant Vocal", human_prefix="Conducteur"),
        )

    def predict(self, input: str):
        return self.conversation.predict(input=input + f" (Taux d'alcoolémie: {self.alcool})")