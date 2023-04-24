from src.menu import *

print(f"{Colors.YELLOW}++++++++++ Console Notes App ++++++++++{Colors.END}")

# main project's loop
while (True):
    menu(LANGUAGE) # printing menu with language's parametr

    choice = input("->  ") # user's choice

    # mechanism to manage choice for main menu
    match(choice):
        case '4': # case for lanugages
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