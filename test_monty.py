import os 

def test_monty_help(): 
    assert(0 == os.system("python3 monty.py --help"))

def test_monty_invalid(): 
    # Antipattern checking this key in, but it's limited to $10 of spend and needs to be present for the tool to be demonstrated
    assert(0 != os.system("python3 monty.py --internal --key='trash key'"))