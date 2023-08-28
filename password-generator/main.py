from password import Password

x = int(input("Podaj length"))
y = int(input("Podaj lower"))
z = int(input("Podaj upper"))
a = int(input("Podaj digit"))
b = int(input("Podaj special"))

test = Password(x, y, z, a, b)

test.create_password()