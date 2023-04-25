from app import *
from menu import *
import os

def new_note():
    rel_directory = os.path.realpath('.')

    filename(LANGUAGE)
    file = input(" -> ")

    # check if file exists
    try:
        f=open(f"{rel_directory}/console-notes-app/notes/{file}.txt","x")
    except FileExistsError:
        print("Error 17!")
    else:
        write_file(LANGUAGE)
        main = input(" -> ")
        f.write(main)


if __name__ == '__main__':
    new_note()
