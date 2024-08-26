from autogen import AssistantAgent, UserProxyAgent

class Agent: 
    """
    Encapsulate a simplified autogen-based agent 
    """

    backend = None
    key = None    
    uri = None

    def __init__(self, system_prompt): 
        """
        Create an instance of the class
        """
        self.system = system_prompt
        pass

    def validate_config(self): 
        """
        Validate the configuration that's been set on this object 
        """
        match self.backend: 
            case "open-ai": 
                if not self.key : 
                    raise Exception(error_prefix + "OpenAI backend requires a key.")
                if self.uri : 
                    raise Exception(error_prefix + "OpenAI backend does not requires a URI.")
            case "ollama": 
                if not self.key or not self.uri: 
                    raise Exception(error_prefix + "Ollama backend requires a URI and key.")
            case "internal": 
                if self.key or self.uri: 
                    raise Exception(error_prefix +"URI or key provided but an internal model was requested, which requires neither!")

    def run(self): 
        """
        Run the agent 

        Returns: 
        Bool: Whether or not the agent terminated unexpectedly. 
        """ 

        self.validate_config()

        llm_config={
            "config_list": [
                {"model": "gpt-4o-mini", "api_key": self.key}
            ]
        }

        print(llm_config)
        assistant = AssistantAgent("monty", llm_config=llm_config)
        assistant.update_system_message(self.system)

        user_proxy = UserProxyAgent("weather-bot", code_execution_config=False)

        # Start the chat
        user_proxy.initiate_chat(
            assistant,
            max_turns=1, 
            message="Today is Sunday, August 25th, 2024. It rained all last week and it's going to rain next week as well. The client lives in North Carolina.",
        )

        return True 

class Gardener(Agent): 
    """
    Encapsulates the state and behavior of an LLM-powered gardening assistant
    """
    system_prompt="""
    You are a curmudgeonly gardening assistant. Given my location, the weather and the current date, \
    you should recommend interventions to keep my garden in top form. You'll only get one shot at the \
    recommendation. You are always terse and limit your responses to 100 characters or less.
    """
    forecast:str = None
    history:str = None

    def __init__(self):
        super().__init__(self.system_prompt)
        pass

    def set_forecast(forecast:str):
        self.forecast = forecast
    
    def set_history(history:str): 
        self.history = history

    def run(self):         
        print("Gardener started!")
        return super().run()
        
