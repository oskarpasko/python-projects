import random

class Password:
    def __init__(self, length, lower, upper, digit, special):
        self.length = length
        self.lower = lower
        self.upper = upper
        self.digit = digit
        self.special = special

    def check_length(self):
        if self.length == (self.lower + self.upper + self.digit + self.special):
            return True
        else: 
            return False
        
    def create_password(self):
        if self.check_length() == True:
            # Code when password's settings are OK

            # Creating an array which will store our password
            password = []

            # Adding random digits to our password
            for _ in range(self.lower):
                password.append(chr(random.randint(97, 122)))
            for _ in range (self.upper):
                password.append(chr(random.randint(65, 90)))
            for _ in range (self.digit):
                password.append(chr(random.randint(48, 57)))
            for _ in range (self.special):
                password.append(chr(random.randint(33, 47)))

            # Code to shuffle chars
            random.shuffle(password)

            # Printing password as a string    
            ready_password = ''
            for x in password:
                ready_password += x

            print("Your password: " + ready_password)
            
        else:
            # Code when password's settings are wrong
            print("Check Your password's settings!")
        