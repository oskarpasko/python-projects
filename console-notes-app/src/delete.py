from menu import *
from settings import *
from switch import *
import os

def delete_note():
    # path to dictionary where we will create and save notes
    rel_directory = os.path.realpath('.')

    file_to_delete(LANGUAGE)
    file = input(" -> ")

    if os.path.exists(f"{rel_directory}/notes/{file}.txt"):
        os.remove(f"{rel_directory}/notes/{file}.txt")
        file_deleted(LANGUAGE)
        
    else: 
        # if file exists we write error
        print(f"{Colors.RED}Error 18!{Colors.END}")

    switch_to_app()

if __name__ == '__main__':
    delete_note()