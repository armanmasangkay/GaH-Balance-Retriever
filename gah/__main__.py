import sys
from .classmodule import MyClass
# from .funcmodule import login
# from .funcmodule import createFile
from .funcmodule import *

def main():
    args = sys.argv[1:]
    for arg in args:
        #balance check 'gah balance'
        if (arg=='balance'):
            login()
        elif (arg=='change'):
            #calling createFile again to change the account details
            createFile()


    
if __name__ == '__main__':
    main()