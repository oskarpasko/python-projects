import os
from settings import *

def delete_note():
    # path to dictionary where we will create and save notes
    rel_directory = os.path.realpath('.')

    file = input(" -> ")

    if os.path.exists(f"{rel_directory}/notes/{file}.txt"):
        os.remove(f"{rel_directory}/notes/{file}.txt")
    else: 
        # if file exists we write error
        print(f"{Colors.RED}Error 18!{Colors.END}")

if __name__ == '__main__':
    delete_note()