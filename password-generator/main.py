from password import Password

setting = []
for x in range(0, 5):
    match(x):
        case 0:
            setting.append(int(input("Input password's length: ")))
        case 1:
            print(f"{setting[0]} characters left.")
            setting.append(int(input("Input how many lower cases: ")))
        case 2:
            print(f"{setting[0]-setting[1]} characters left.")
            setting.append(int(input("Input how many upper cases: ")))
        case 3:
            print(f"{setting[0]-setting[1]-setting[2]} characters left.")
            setting.append(int(input("Input how many digits: ")))
        case 4:
            print(f"{setting[0]-setting[1]-setting[2]-setting[3]} characters left.")
            setting.append(int(input("Input how many special characters: ")))

test = Password(setting[0], setting[1], setting[2], setting[3], setting[4])

test.create_password()