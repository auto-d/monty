import time
import argparse
import agent

def main(args): 
    """
    Application entry point 
    """
    try: 
        monty = agent.Gardener()

        monty.backened = args.backend
        monty.key = args.key
        monty.uri = args.uri

        monty.run('Could use some recommendations on garden chores today!', args.max_turns)
    
    except Exception as e: 
        print(e)

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        description="CLI for instantiating and interacting with the gardening agent."
        ) 
    parser.add_argument("--backend", required=True, help="backend LLM to use for the agent",
        choices=[
            "open-ai", 
            "ollama", 
            "internal"
        ]) 
    parser.add_argument("--key", help="API key to use for LLM backend")
    parser.add_argument("--uri", help="URI (ip:port/path) of LLM API")
    parser.add_argument("--max-turns", help="Maximum number of turns to interact with monty")
    
    args = parser.parse_args() 

    main(args) 