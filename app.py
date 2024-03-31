from VigilAuto.config.configuration import ConfigurationManager
from VigilAuto.components.llm import LLM
from VigilAuto import logger

def main():
    config_manager = ConfigurationManager()
    llm_config = config_manager.get_llm_config()
    llm = LLM(config=llm_config)
    logger.info("LLM model loaded successfully")
    print(llm.get_response("J'ai bu quelques verres, mais je me sens bien pour conduire."))

if __name__ == "__main__":
    main()