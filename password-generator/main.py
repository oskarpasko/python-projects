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
            print("Ok")
        else:
            print("Nope")

x = int(input("Podaj length"))
y = int(input("Podja lower"))
z = int(input("Podaj upper"))
a = int(input("Podaj digit"))
b = int(input("Podaj special"))

test = Password(x, y, z, a, b)

test.create_password()