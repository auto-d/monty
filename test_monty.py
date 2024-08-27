import os 

def test_monty_help(): 
    assert(0 == os.system("python3 monty.py --help"))

def test_monty_valid(): 
    assert(0 == os.system("python3 monty.py --backend=open-ai --key='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'"))

def test_monty_invalid(): 
    # Antipattern checking this key in, but it's limited to $10 of spend and needs to be present for the tool to be demonstrated
    assert(0 != os.system("python3 monty.py --internal --key='trash key'"))