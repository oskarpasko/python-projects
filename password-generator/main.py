from password import Password
from settings import Colors

setting = []
for x in range(0, 5):
    match(x):
        case 0:
            setting.append(int(input(f"{Colors.CYAN}Input password's length: ")))
            print()
        case 1:
            print(f"{Colors.LIGHT_GREEN}{setting[0]} characters left.")
            setting.append(int(input(f"{Colors.CYAN}Input how many lower cases: ")))
            print()
        case 2:
            print(f"{Colors.LIGHT_GREEN}{setting[0]-setting[1]} characters left.")
            setting.append(int(input(f"{Colors.CYAN}Input how many upper cases: ")))
            print()
        case 3:
            print(f"{Colors.LIGHT_GREEN}{setting[0]-setting[1]-setting[2]} characters left.")
            setting.append(int(input(f"{Colors.CYAN}Input how many digits: ")))
            print()
        case 4:
            print(f"{Colors.LIGHT_GREEN}{setting[0]-setting[1]-setting[2]-setting[3]} characters left.")
            setting.append(int(input(f"{Colors.CYAN}Input how many special characters: {Colors.END}")))
            print()

test = Password(setting[0], setting[1], setting[2], setting[3], setting[4])

test.create_password()