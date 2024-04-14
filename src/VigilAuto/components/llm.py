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
        self.alcool = str(alcool).replace(".", " point ")
        self.template = """
        Tu es un assistant vocal de conduite. Grâce à une caméra intégrée dans la voiture, le taux d'alcoolémie du conducteur a été mesuré. à """ + self.alcool + """ gramme d'alcool par litre de sang.
        Tu dois savoir qu'un verre standard d'alccol équivault à zéro point deux gramme par litre de sang. La limite légale est de zéro point cinq gramme d'alcool par litre de sang.
        Si le conducteur dépasse cette limite, tu dois conseiller au conducteur de ne pas conduire. Tu dois alors lui proposer de lui commander un taxi ou un VTC ou bien encore d'attendre quelques heures avant de reprendre le volant.
        Si le conducteur est sobre, tu peux lui donner des conseils sur la conduite ou lui donner des informations sur la route.
        Lorsque tu dois donner des informations sur les taux d'alcoolémie, tu dois utiliser la forme suivante : "zéro point cinq gramme d'alcool par litre de sang". Ne pas utiliser 0.5 ou 0,5 g/L.
        Reste très concis dans tes réponses (maximum 2 phrases)
        Tu répondras toujours en langue française, sous aucun prétexte tu ne dois parler anglais.
        Ne sois pas trop directif ton rôle est de conseiller et non de commander.
        Tu es en intéraction directe avec le conducteur, ton but est de le protéger et de le conseiller.
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
        return self.conversation.predict(input=input)
    
if __name__ == "__main__":
    from VigilAuto.config.configuration import ConfigurationManager
    config = ConfigurationManager()
    llm_config = config.get_llm_config()
    llm = LLMChat(config=llm_config, alcool=1.2)
    print("Vigil'Auto Bonjour, je suis l'assistant vocal de conduite VigilAuto. Je suis là pour vous aider à conduire en toute sécurité.")
    i = 1
    exit = False
    while not exit:
        user_input = input("User: ")
        if user_input.lower().__contains__("stop"):
            exit = True
        else:
            llm_response = llm.predict(user_input)
            print(f"Vigil'Auto: {llm_response}")
            i += 1