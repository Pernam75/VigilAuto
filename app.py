from VigilAuto.config.configuration import ConfigurationManager
from VigilAuto.components.llm import LLMChat
from VigilAuto.components.tts import TTS

if __name__ == "__main__":
    config = ConfigurationManager()

    llm_config = config.get_llm_config()
    tts_config = config.get_tts_config()

    llm = LLMChat(config=llm_config, alcool=0.5)
    tts = TTS(config=tts_config)

    i = 0
    exit = False

    while not exit:
        user_input = input("User: ")
        llm_response = llm.predict(user_input)
        print(f"Assistant Vocal: {llm_response}")
        tts.synthetize(llm_response, f"{i}_test")
        i += 1
        if user_input.lower().__contains__("stop"):
            exit = True
            print("Exiting...")
