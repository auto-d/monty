import time
import argparse
import agent

# source based on pattern suggested in https://www.coursera.org/learn/python-mlops-duke/lecture/oFMaa/using-the-argparse-framework
def main(): 
    monty = agent.Gardener()
    monty.run()

if __name__ == '__main__': 
    parser = argparse.ArgumentParser(
        description="CLI for instantiating and interacting with the monty gardening agent."
        ) 
    #parser.add_argument("--arg", help="an argument you can pass", type=int, choices=[1,2,3]) 
    #parser.add_argument("-f", "--flag", help="a flag you can set", action="store_true")     
    
    args = parser.parse_args() 

    main() 