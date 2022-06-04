import random
import os
import mouse
import keyboard
import time

def logo():
    z = random.randint(0,7)
    os.system(f"color {z}")
    print("  ██████  █    ██  ███▄    █  ██▀███   ██▓  ██████ ▓█████ ")
    print("▒██    ▒  ██  ▓██▒ ██ ▀█   █ ▓██ ▒ ██▒▓██▒▒██    ▒ ▓█   ▀ ")
    print("░ ▓██▄   ▓██  ▒██░▓██  ▀█ ██▒▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒███   ")
    print("  ▒   ██▒▓▓█  ░██░▓██▒  ▐▌██▒▒██▀▀█▄  ░██░  ▒   ██▒▒▓█  ▄ ")
    print("▒██████▒▒▒▒█████▓ ▒██░   ▓██░░██▓ ▒██▒░██░▒██████▒▒░▒████▒")
    print("▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░")
    print("░ ░▒  ░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░  ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░ ░ ░  ░")
    print("░  ░  ░   ░░░ ░ ░    ░   ░ ░   ░░   ░  ▒ ░░  ░  ░     ░   ")
    print("      ░     ░              ░    ░      ░        ░     ░  ░")
    print("Made by Headshot56#6069 and helped by Wallaby\n")

logo()

def random_2d(low, upp):
    low = list(str(low))
    upp = list(str(upp))
    if len(low) != 4:
        for i in range(4 - len(low)):
            low.append("1")
    if len(upp) != 4:
        for i in range(4 - len(upp)):
            upp.append("1")

    try:
        p1 = random.randint(int(low[0]), int(upp[0]))
    except:
        p1 = random.randint(int(upp[0]), int(low[0]))
    try:
        p2 = random.randint(int(low[2]), int(upp[2]))
    except:
        p2 = random.randint(int(upp[2]), int(low[2]))
    try:
        p3 = random.randint(int(low[3]), int(upp[3]))
    except:
        p3 = random.randint(int(upp[3]), int(low[3]))
    
    return float(f"{p1}.{p2}{p3}")

while True:
    os.system("cls")
    logo()
    menu = -69420
    while menu != 1 and menu != 2 and menu != 3:
        try:
            menu = int(input("1.Clicker\n2.Settings\n3.Prefabs\n"))
            if menu == 1:
                #Clicker menu
                print(f"Please press your selected keybind to click. To go back to the other settings press ctrl-c")
                if wait_timeL < 0.01:
                    wait_timeL = 0.01
                if wait_timeU > 9.99:
                    wait_timeU = 9.99
                if toggle == 2:
                    while True:
                        if keyboard.is_pressed(keybind):
                            wait_time = random_2d(wait_timeL, wait_timeU)
                            time.sleep(wait_time)
                            if cbutton == 2:
                                mouse.click('right')
                            else:
                                mouse.click()
                if toggle == 1:
                    while True:
                        on = False
                        if keyboard.is_pressed(keybind):
                            on = True
                        if on == True:
                            while keyboard.is_pressed(keybind) != True:
                                wait_time = random_2d(wait_timeL, wait_timeU)
                                time.sleep(wait_time)
                                if cbutton == 2:
                                    mouse.click('right')
                                else:
                                    mouse.click()

            elif menu == 2:
                #Settings menu
                try:
                    toggle = int(input("1.Toggle\n2.Press and hold\n"))
                    cbutton = int(input("1.Left Click\n2.Right Click\n"))
                    keybind = input("What key would you like to activate your autoclicker: ")
                    print("The fastest time allowed is 0.01 seconds slowest is 9.99. Make sure your upper bound is different than your lower")
                    wait_timeL = float(input("Lower bound of wait time in seconds(ex- 0.01): "))
                    wait_timeL = float(format(wait_timeL, ".2f"))
                    wait_timeU = float(input("Upper bound of wait time in seconds(ex- 9.99): "))
                    wait_timeU = float(format(wait_timeU, ".2f"))
                    input("Settings finished - Press enter to continue. . .")
                except:
                    input("Please input the correct things!")
            elif menu == 3:
                #Prefabs menu
                ly = int(input("1.Load a prefab\n2.Save current settings to a prefab\n"))
                try:
                    if ly == 1:
                        filenam = input("What is the name of the config: ")
                        with open(f"{filenam}.sun", "r+") as file:
                            unformatted = file.read()
                            listd = unformatted.split("-")
                            keybind = listd[0]
                            wait_timeL = float(listd[1])
                            wait_timeU = float(listd[2])
                            toggle = int(listd[3])
                            cbutton = int(listd[4])
                            input(f"Succesfully loaded config: {filenam}.sun\nPress enter to continue")
                    elif ly == 2:
                        filenam = input("What is the name of the config: ")
                        with open(f"{filenam}.sun", "w+") as file:
                            formatted_data = f"{keybind}-{wait_timeL}-{wait_timeU}-{toggle}-{cbutton}"
                            file.write(formatted_data)
                            input(f"Succesfully saved config: {filenam}.sun\nPress enter to continue")
                except:
                    input("Something went wrong... if this problem persists check your config or contact the devs")

            else:
                input("Press Enter to continue")
                os.system("cls")
                logo()
        except:
            input("Please type a number to select")
            os.system("cls")
            logo()