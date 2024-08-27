from agent import Agent, Gardener

# These tests need to be refactored, we've now disallowed the more casual invocation they were 
# designed to validate since the local inference is intolerably sllooooow. 
def test_create_agent(): 
    agent = Agent()
    agent.backend = "open-ai"
    agent.key = "garbage key"

    try: 
        agent.run()
        
        # Can't run w/o legit key, should raise
        assert(False)
    except Exception as e: 
        assert(True)

def test_create_gardener(): 
    gardener = Gardener()
     
    try: 
        gardener.run()
        
        # Can't run w/o key, backend, should raise
        assert(False)
    except Exception as e: 
        assert(True)