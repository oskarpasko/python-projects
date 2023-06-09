from pymongo import MongoClient
from getpass import getpass
from settings import *
import pprint

# db connection
client = MongoClient("mongodb://localhost:27017")
db = client.loginData
users = db.user

# main loop of register / login
while True:

    # main menu
    print(f"{Colors.YELLOW}\n ---------- Main Page ---------- \n{Colors.END}")
    print(f"{Colors.LIGHT_PURPLE}1. Login{Colors.END}")
    print(f"{Colors.LIGHT_PURPLE}2. Register{Colors.END}")
    print(f"{Colors.LIGHT_PURPLE}3. Exit{Colors.END}")

    # users choice
    choice = input()  

    match(choice):
        case '1':  # case to login user
            print(f"{Colors.YELLOW}\n ---------- Login Page ---------- \n{Colors.END}")
            print(f'{Colors.GREEN}If you wan to exit write "exit" in login.{Colors.END}')

            # get login
            login = input(f"{Colors.BLUE}Insert Your login: {Colors.END}")

            # if login == exit then end a program
            if login == 'exit':
                exit(f"{Colors.PURPLE}Bye, have a great time!{Colors.END}")

            # get password
            password = getpass(f"{Colors.BLUE}Insert Your password: {Colors.END}")

            # get data from db
            temp = users.find_one({'login': f'{login}', 'password': f'{password}'})

            # check if record exists
            if temp == None:
                print(f"{Colors.RED}\nWrong login or password!{Colors.END}")
            else:
                break

        case '2':  # case to register user
            print(f"{Colors.YELLOW}\n ---------- Register Page ---------- \n{Colors.END}")
            
            # get first name
            first_name = input(f"{Colors.BLUE}Insert Your first name: {Colors.END}")

            # get last name
            last_name = input(f"{Colors.BLUE}Insert Your last name: {Colors.END}")

            # get login
            login = input(f"{Colors.BLUE}Insert Your login: {Colors.END}")

            # get password
            password = getpass(f"{Colors.BLUE}Insert Your password: {Colors.END}")

            # repeat the password
            r_password = getpass(f"{Colors.BLUE}Repeat Your password: {Colors.END}")

            if password != r_password:
                print(f"{Colors.RED}\nPasswords are not equal!{Colors.END}")
            else:
                # user's data
                data = {'login': f'{login}',
                        'password': f'{password}',
                        'details': {
                            'fname': f'{first_name}',
                            'lname': f'{last_name}'
                            },
                        'status': 'user',
                        }
                
                # register new user
                new_user = users.insert_one(data)


        case '3':  # case to exit from the program
            exit(f"{Colors.PURPLE}Bye, have a great time!{Colors.END}")
        case _:
                print(f"{Colors.RED}ERROR 12!{Colors.END}")

# code after user was logged
while True:
    print(f"{Colors.YELLOW}\n ---------- Main Page ---------- \n{Colors.END}")

    # get data logged user
    user = users.find_one({'login': f'{login}', 'password': f'{password}'})
    details = user['details']
    print(f"{Colors.CYAN}\nWelcome back {details['fname']}!{Colors.END}")

    # menu for admin user
    if user['status'] == 'admin':

        # ---------- Admin panel ----------

        print(f"{Colors.LIGHT_PURPLE}1. Show all users{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}2. Update user{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}3. Delete user{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}4. Exit{Colors.END}")

        # users choice
        choice = input()  

        match(choice):
            case '1': # Update user account
                print(f"{Colors.YELLOW}\n ----- All Users ----- \n{Colors.END}")

                write_users = users.find()

                for user in write_users:
                    details = user['details']
                    print(f"{Colors.LIGHT_RED}ID: {user['_id']}{Colors.END}")
                    print(f"{Colors.LIGHT_GREEN}Login:{Colors.END} {Colors.ITALIC}{user['login']}{Colors.END}")
                    print(f"{Colors.LIGHT_GREEN}First name:{Colors.END} {details['fname']}")
                    print(f"{Colors.LIGHT_GREEN}Last name:{Colors.END} {details['lname']}")
                    print(f"\n ------------------------------ \n")

            case '2':
                print(f"{Colors.YELLOW}\n ----- Update User ----- \n{Colors.END}")

                # get login which user we wanna change
                user_to_change = input(f'{Colors.GREEN}Which user (login) You would like to change: {Colors.END}')

                # menu
                print(f'{Colors.GREEN}What You want to change?{Colors.END}')
                print(f"{Colors.LIGHT_PURPLE}1. Login{Colors.END}")
                print(f"{Colors.LIGHT_PURPLE}2. First name{Colors.END}")
                print(f"{Colors.LIGHT_PURPLE}3. Last Name{Colors.END}")

                # user choice
                choice = input()

                match(choice):
                    case '1': # change login

                        # insert new login
                        login_to_change = input(f"{Colors.BLUE}Insert new login: {Colors.END}")

                        # update login in database
                        users.update_one({'login': user_to_change},
                                         { "$set": { "login": login_to_change }})
                        
                    case '2': # change first name

                        # insert new first name
                        fname_to_change = input(f"{Colors.BLUE}Insert new first name: {Colors.END}")

                        # save user's details for later
                        details = users.find_one({'login': f'{user_to_change}'})['details']

                        # update first name and add last name to query
                        users.update_one({'login': user_to_change}, 
                                         { "$set": { "details": {'fname': fname_to_change, 
                                                                                            'lname': details['lname']}}})
                    case '3': # chagne last name

                        # insert last name
                        lname_to_change = input(f"{Colors.BLUE}Insert new last name: {Colors.END}")

                        # save user's details for later
                        details = users.find_one({'login': f'{user_to_change}'})['details']

                        # update last name and add first name to query
                        users.update_one({'login': user_to_change},
                                         { "$set": { "details": {'fname': details['fname'], 
                                                                 'lname': lname_to_change} }})
            case '4':
                exit()
            case _:
                print(f"{Colors.RED}ERROR 12!{Colors.END}")
    else:

        # ---------- Admin panel ----------

        print(f"{Colors.LIGHT_PURPLE}1. Update account{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}2. Delete account{Colors.END}")
        print(f"{Colors.LIGHT_PURPLE}3. Exit{Colors.END}")

        choice = input()  # users choice

        match(choice):
            case '1':  # Update user account
                print(f"{Colors.YELLOW}\n ----- Update Account ----- \n{Colors.END}")

                # get logged user login
                user_to_change = user['login']

                # menu to choose
                print(f'{Colors.GREEN}What You want to change?{Colors.END}')
                print(f"{Colors.LIGHT_PURPLE}1. Login{Colors.END}")
                print(f"{Colors.LIGHT_PURPLE}2. First name{Colors.END}")
                print(f"{Colors.LIGHT_PURPLE}3. Last Name{Colors.END}")
                choice = input()

                match(choice):
                    case '1': # change login

                        # insert new login
                        login_to_change = input(f"{Colors.BLUE}Insert new login: {Colors.END}")
                        
                        # update login in database
                        users.update_one({'login': user_to_change},
                                         { "$set": { "login": login_to_change }})
                        
                        # exit from application cause user have to log in one more time
                        exit(f"{Colors.PURPLE}Login one more time!{Colors.END}")

                    case '2': # change first name

                        # insert new first name
                        fname_to_change = input(f"{Colors.BLUE}Insert new first name: {Colors.END}")

                        # get user's details for later
                        details = users.find_one({'login': f'{user_to_change}'})['details']

                        # update first name and add last name to query
                        users.update_one({'login': user_to_change}, 
                                         { "$set": { "details": {'fname': fname_to_change, 
                                                                 'lname': details['lname']}}})
                    
                    case '3': # change last name

                        # insert new last name
                        lname_to_change = input(f"{Colors.BLUE}Insert new last name: {Colors.END}")

                        # get user's details for later
                        details = users.find_one({'login': f'{user_to_change}'})['details']

                        # update last name and add first name to query
                        users.update_one({'login': user_to_change},
                                         { "$set": { "details": {'fname': details['fname'], 
                                                                 'lname': lname_to_change} }})
            case '2': # delete account
                print(f"{Colors.YELLOW}\n ----- Delete Account ----- \n{Colors.END}")
                print(f'{Colors.GREEN}To delete account insert Your password.{Colors.END}')

                # get password to confirm deleting account
                password_to_delete = getpass(" -> ")

                # checking if password is correct
                if password_to_delete == user['password']:
                    # deleting account and exiting from aplication
                    users.delete_one({'login': user['login']})
                    exit(f"{Colors.PURPLE}Bye, have a great time!{Colors.END}")
                else: 
                    print(f"{Colors.RED}\nWrong password!{Colors.END}")

            case '3':
                exit()
            case _:
                print(f"{Colors.RED}ERROR 12!{Colors.END}")
