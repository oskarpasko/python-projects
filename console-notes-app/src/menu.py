from settings import *

# variable to know which language user want to use
LANGUAGE = 'pl'

# function which printing menu with specific language
def menu(lang):
    if(lang == 'pl'): _menu_pl()
    if(lang == 'eng'): _menu_eng()

# polish menu
def _menu_pl():
    print(f"{Colors.LIGHT_BLUE}1. Nowa notatka")
    print("2. Czytaj notatki")
    print("3. Usuń notatkę")
    print("4. Język")
    print(f"5. Wyjdź{Colors.END}")

# english menu
def _menu_eng():
    print(f"{Colors.LIGHT_BLUE}1. New note")
    print("2. Write notes")
    print("3. Delete note")
    print("4. Language")
    print(f"5. Quit{Colors.END}")

def filename(lang):
    if(lang == 'pl'): _filename_pl()
    if(lang == 'eng'): _filename_eng()

def _filename_pl():
    print(f"{Colors.CYAN}Podaj nazwę pliku: {Colors.END}")

def _filename_eng():
    print(f"{Colors.CYAN}Name Your file:  {Colors.END}")

def write_file(lang):
    if(lang == 'pl'): _write_filename_pl()
    if(lang == 'eng'): _write_filename_eng()

def _write_filename_pl():
    print(f"{Colors.CYAN}Napisz swoją notatkę: {Colors.END}")

def _write_filename_eng():
    print(f"{Colors.CYAN}Write Your note: {Colors.END}")

def file_saved(lang):
    if(lang == 'pl'): file_saved_pl()
    if(lang == 'eng'): file_saved_eng()

def file_saved_pl():
    print(f"{Colors.CYAN}Zapisano notatkę:  {Colors.END}")

def file_saved_eng():
    print(f"{Colors.CYAN}Note was saved:  {Colors.END}")

def file_deleted(lang):
    if(lang == 'pl'): file_deleted_pl()
    if(lang == 'eng'): file_deleted_eng()

def file_deleted_pl():
    print(f"{Colors.CYAN}Usunięto notatkę:  {Colors.END}")

def file_deleted_eng():
    print(f"{Colors.CYAN}Note was deleted:  {Colors.END}")

def file_to_delete(lang):
    if(lang == 'pl'): file_to_delete_pl()
    if(lang == 'eng'): file_to_delete_eng()

def file_to_delete_pl():
    print(f"{Colors.CYAN}Która notatkę chcesz usunąć:  {Colors.END}")

def file_to_delete_eng():
    print(f"{Colors.CYAN}Which note would You like to delete:  {Colors.END}")
    