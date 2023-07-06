from pymongo import MongoClient
from getpass import getpass
from settings import *

client = MongoClient("mongodb://localhost:27017")
db = client.loginData
users = db.user

while True:
    print(f"{Colors.YELLOW}\n ---------- Login Page ---------- \n{Colors.END}")
    print(f'{Colors.GREEN}If you wan to exit write "exit" in login.{Colors.END}')
    login = input(f"{Colors.BLUE}Insert Your login: {Colors.END}")
    if login == 'exit': exit(f"{Colors.PURPLE}Bye, have a great time!{Colors.END}")
    password = getpass(f"{Colors.BLUE}Insert Your password: {Colors.END}")

    temp = users.find_one({'login': f'{login}', 'password': f'{password}'})

    if temp == None:
        print(f"{Colors.RED}\nWrong login or password!{Colors.END}")
    else:
        break
user = users.find_one({'login': f'{login}', 'password': f'{password}'})
details = user['details']
print(f"{Colors.CYAN}\nWelcome back {details['fname']}!{Colors.END}")
