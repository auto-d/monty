import time
import argparse
import agent

def main(args): 
    """
    Gardener agent entry point 
    """

    monty = agent.Gardener()
    monty.run()

def validate_args(args): 
    """
    Validate the arguments 
    """
    valid = False
    error_prefix = "error: "
    match args.backend: 
        case "open-ai": 
            if args.key and args.uri: 
                valid = True 
            else: 
                print(error_prefix, "OpenAI backend requires a URI and key.")
        case "ollama": 
            if args.key and args.uri: 
                valid = True 
            else: 
                print(error_prefix, "Ollama backend requires a URI and key.")
        case "internal": 
            if not args.key and not args.uri: 
                valid = True
            else: 
                print(error_prefix, "URI or key provided but an internal model was requested!")

    return valid

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
    
    args = parser.parse_args() 

    if validate_args(args):
        main(args) 