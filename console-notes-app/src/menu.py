from .settings import *

LANGUAGE = 'pl'

def menu(lang):
    if(lang == 'pl'): menu_pl()
    if(lang == 'eng'): menu_eng()

def menu_pl():
    print(f"{Colors.LIGHT_BLUE}1. Nowa notatka")
    print("2. Czytaj notatki")
    print("3. Usuń notatkę")
    print("4. Język")
    print(f"5. Wyjdź{Colors.END}")

def menu_eng():
    print(f"{Colors.LIGHT_BLUE}1. New note")
    print("2. Write notes")
    print("3. Delete note")
    print("4. Language")
    print(f"5. Quit{Colors.END}")
    