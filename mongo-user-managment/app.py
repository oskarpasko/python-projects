from pymongo import MongoClient
from getpass import getpass

client = MongoClient("mongodb://localhost:27017")
db = client.loginData
users = db.user

while True:
    print("\n ---------- Login Page ---------- \n")
    print('If you wan to exit write "exit" in login.')
    login = input("Insert Your login: ")
    if login == 'exit': exit("Bye, have a great time!")
    password = getpass("Insert Your password: ")

    temp = users.find_one({'login': f'{login}', 'password': f'{password}'})

    if temp == None:
        print("Wrong login or password!")
    else:
        user = users.find_one({'login': f'{login}', 'password': f'{password}'})
        details = user['details']
        print(f"Welcome back {details['fname']}!")
