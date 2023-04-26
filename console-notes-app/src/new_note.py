from menu import *
from settings import *
from switch import *
import os

def new_note():
    # path to dictionary where we will create and save notes
    rel_directory = os.path.realpath('.')

    # question for file's name
    filename(LANGUAGE)
    file = input(" -> ")

    # check if file exists
    try:
        # we are creating file
        f=open(f"{rel_directory}/notes/{file}.txt","x")
    except FileExistsError:
        # if file exists we write error
        print(f"{Colors.RED}Error 17!{Colors.END}")
    else:
        # we ask to write some note for user and then we save file
        write_file(LANGUAGE)
        main = input(" -> ")
        f.write(main)
        file_saved(LANGUAGE)

        switch_to_app()


if __name__ == '__main__':
    new_note()
