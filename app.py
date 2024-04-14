from VigilAuto.config.configuration import ConfigurationManager
from VigilAuto.components.llm import LLMChat
from VigilAuto.components.tts import TTS
from pydub import AudioSegment
from pydub.playback import play

if __name__ == "__main__":
    config = ConfigurationManager()

    alcool = 0.6

    llm_config = config.get_llm_config()
    tts_config = config.get_tts_config()

    llm = LLMChat(config=llm_config, alcool=alcool)
    tts = TTS(config=tts_config)

    print("Vigil'Auto Bonjour, je suis l'assistant vocal de conduite VigilAuto. Je suis là pour vous aider à conduire en toute sécurité.")
    output_path = tts.synthetize("Bonjour, je suis l'assistant vocal de conduite VigilAuto. Je suis là pour vous aider à conduire en toute sécurité.", "0_test")
    song = AudioSegment.from_mp3(output_path)
    play(song)
    with open(f"traces_archive/{alcool}.txt", "w") as f:
        f.write("Vigil'Auto: Bonjour, je suis l'assistant vocal de conduite VigilAuto. Je suis là pour vous aider à conduire en toute sécurité.\n")
    i = 1
    exit = False
    while not exit:
        user_input = input("User: ")
        if user_input.lower().__contains__("stop"): # TODO 1 : the stop condition must be changed to an intent detection system
            exit = True
        else:
            llm_response = llm.predict(user_input)
            with open(f"traces_archive/{alcool}.txt", "a") as f:
                f.write(f"User: {user_input}\n")
                f.write(f"Vigil'Auto: {llm_response}\n")
            output_path = tts.synthetize(llm_response, f"{i}_test")
            song = AudioSegment.from_mp3(output_path)
            play(song)
            i += 1
