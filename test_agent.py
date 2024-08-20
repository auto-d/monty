from agent import Agent, Gardener

def test_create_agent(): 
    agent = Agent()
    assert(agent.run() == True)

def test_create_gardener(): 
    gardener = Gardener()
    assert(gardener.run() == True)