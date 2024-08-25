import os 

def test_monty(): 
    success = True
    
    try: 
        if (0 != os.system("python3 monty.py --help")): 
            success = False

    except: 
        success = False

    assert(success == True)