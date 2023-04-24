from .settings import *

# variable to know which language user want to use
LANGUAGE = 'pl'

# function which printing menu with specific language
def menu(lang):
    if(lang == 'pl'): menu_pl()
    if(lang == 'eng'): menu_eng()

# polish menu
def menu_pl():
    print(f"{Colors.LIGHT_BLUE}1. Nowa notatka")
    print("2. Czytaj notatki")
    print("3. Usuń notatkę")
    print("4. Język")
    print(f"5. Wyjdź{Colors.END}")

# english menu
def menu_eng():
    print(f"{Colors.LIGHT_BLUE}1. New note")
    print("2. Write notes")
    print("3. Delete note")
    print("4. Language")
    print(f"5. Quit{Colors.END}")
    