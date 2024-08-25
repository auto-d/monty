class Agent: 
    """
    Encapsulate a simplified autogen-based agent 
    """

    def __init__(self): 
        """
        Create an instance of the class
        """
        pass

    def run(self): 
        """
        Run the agent 

        Returns: 
        Bool: Whether or not the agent terminated unexpectedly. 
        """ 
        print("Agent started!")
        return True 

class Gardener(Agent): 
    """ 
    Encapsulates the state and behavior of an LLM-powered gardening assistant
    """

    def __init__(self): 
        pass

    def run(self):         
        print("Gardener started!")
        return super().run()
        
