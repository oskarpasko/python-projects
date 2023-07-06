from pymongo import MongoClient
from getpass import getpass

client = MongoClient("mongodb://localhost:27017")
db = client.loginData
users = db.user

print(" ---------- Login Page ---------- \n")
login = input("Insert Your login: ")
password = getpass("Insert Your password: ")

temp = users.find_one({'login': f'{login}', 'password': f'{password}'})

if temp == None:
    print("Wrong login or password!")
else:
    user = users.find_one({'login': f'{login}', 'password': f'{password}'})
    details = user['details']
    print(f"Welcome back {details['fname']}!")
