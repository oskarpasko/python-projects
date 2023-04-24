from src.menu import *

print(f"{Colors.YELLOW}++++++++++ Console Notes App ++++++++++{Colors.END}")

while (True):
    menu(LANGUAGE)

    choice = input("->  ")

    match(choice):
        case '4':
            print(f"{Colors.BLUE}1. Polski")
            print(f"2. English{Colors.END}")
            lang_choice = input("-> ")
            match(lang_choice):
                case '1':
                    LANGUAGE = 'pl'
                case '2':
                    LANGUAGE = 'eng'
                case _:
                    print(f"{Colors.RED}Error 12!{Colors.END}")