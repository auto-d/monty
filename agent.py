from autogen import AssistantAgent, UserProxyAgent

class Agent: 
    """
    Encapsulate a simplified autogen-based agent 
    """

    backend = None
    key = None    
    uri = None

    def __init__(self, system_prompt="You are a helpful assistant."): 
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

    def run(self, prompt, max_turns=1): 
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

        assistant = AssistantAgent("monty", llm_config=llm_config)
        assistant.update_system_message(self.system)

        user_proxy = UserProxyAgent("weather-bot", code_execution_config=False)

        # Start the chat
        user_proxy.initiate_chat(
            assistant,
            max_turns=max_turns, 
            message=prompt,
        )

        return True 

import weather
import datetime

class Gardener(Agent): 
    """
    Encapsulates the state and behavior of a toy LLM-powered gardener and a 
    """
    
    system_prompt=\
    """You are a curmudgeonly gardening assistant. Given the current date, historical precipitation, the forecast \
    and a location, you should recommend interventions to keep the client's garden in top form. You are always terse \
    and limit your responses to 200 characters or less."""
    geo:weather.IPGeo = None
    forecast:weather.Forecast = None
    precip:weather.Precipitation = None

    retrospective_days = 2

    def __init__(self):
        super().__init__(self.system_prompt)
        
        print("--------------------------------------------------------------------------------")
        print("Doing some background research to furnish to your gardener (monty).")
        
        self.geo = weather.IPGeo()
        
        self.forecast = weather.Forecast()
        self.forecast.resolve_location(self.geo.lat, self.geo.lon)
        self.forecast.update_forecast()

        self.precip = weather.Precipitation()
        self.precip.update_precipitation(self.geo.zip, self.retrospective_days)

    def format_date(self): 
        today = datetime.date.today() 
        return f"Today is {today.strftime("%Y-%m-%d")}."
    
    def format_precip(self): 
        text = "There is no historical precipitation available."

        if len(self.precip.precip) != 0: 
            text = f"Here are the last {self.retrospective_days} days worth of precipitation:\n"
            for p in self.precip.precip: 
                text = text + ' - ' + f"{p['precip_inches']}\" on {p['date']}" + '\n' 
        
        return text
    
    def format_forecast(self): 
        text = '' 
        for f in self.forecast.forecast: 
            text = text + ' - ' + f + '\n'
        return f"The forecast for next week is:\n{text}\n"

    def format_location(self): 
        return f"The client lives in {self.geo.city}, {self.geo.state}."
    
    def run(self, prompt='', max_turns=1):
        print("Gardener started!")
        print(" ! Ignore subsequent API key warning, autogen validation routine is outdated. (╯°□°)╯")

        macro_prompt=self.format_date() + " " \
            + self.format_precip() + " " \
            + self.format_forecast() + " " \
            + self.format_location() + " " \
            + prompt
        
        return super().run(macro_prompt, max_turns)