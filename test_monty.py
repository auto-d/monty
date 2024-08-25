import os 

def test_monty(): 

    try: 
        # Good usage... 
        assert(0 == os.system("python3 monty.py --help"))
        
        # Bad usage, should bail
        assert(0 != os.system("python3 monty.py --internal --key='asdkjf;aads'"))
        assert(0 != os.system("python3 monty.py --openai"))
        assert(0 != os.system("python3 monty.py --ollama"))

    except: 
        assert(False)