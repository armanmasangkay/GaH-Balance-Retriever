import sys
from .classmodule import MyClass
from .funcmodule import login
from .funcmodule import createFile

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
        #balance check 'gah balance'
        if (arg=='balance'):
            login()
            #createFile()


    
if __name__ == '__main__':
    main()