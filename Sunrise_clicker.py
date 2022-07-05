import random
import os
import mouse
import keyboard
import time
from ctypes.wintypes import PSHORT
from httplib2 import Credentials
import psutil, platform, GPUtil
from hashlib import md5
import requests 
import gspread
Credentials = {
    "type": "service_account",
    "project_id": "spreadsheet-352910",
    "private_key_id": "34aa40140b3d5e63c8ef572671df498f6359b8df",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDsEkF45mZZf3JH\nbndQhRVo6ePKNlH7sJ3bZO0PHVWUBkUAa5evLGBe4cdXYe+bKB0bdful58qysTRG\nSp7hfrmJ3J5j3juk9bOP54sQOYhg4uK0TOdf2ZSo9hJGvJFPmJGnwmn5RheaVY5N\ncC3NPbjm5JcSZFglg6PUgCSyN+WjAAgFdyZ7dSRi9bgkU7K7xljXBiOOKXMb8dyv\neNieoj5U+p11DyfcCwD3tK04ya2tdal0Nz1JjxY/GdCVuepwgJxPGBgmNWuI+YSV\nE1KpTIwj8wJJXxdqBUbaVkr2MNOkpvitje4tB0RNTjbvlYcQ9ToUsqH2oXnw4OSp\nYdYGmmslAgMBAAECggEAEteelMnkngmCmeBfmWeUUf3mueA3dfZFLnQ+4zraEEkN\nBXlEL6ERBhgeSZBRe00qpmNdFRzMCUXRYGtNuCQQ864bKrYO66rV/+S6xq4/TBn/\n5bIEfucgEV/zc7FSv3HAunOiWSYDj0SutlAywuCsAZETdjSlJniV2uNP5BuuPzuD\npQeZnvkuxqM32eomwjtpYQn0VM97TBhz3XEI0llIP0PIaYMnumPrS8LIgOLwO/z9\nVx0LQeMUDENcg18yNTpnHLyPdRdbS9XR31OOdBeUsEi6tNtjw0OSVdD7J+H+clkc\nR8eOrMe6FPmXi18zCJzHO0USXpZxo7qAsEFDa8LR9wKBgQD9uXI0FOJEfRDB9h4T\nXaAxYqdRoXGFZhFGo7UbHRz7WYg1d5b3/+mfnVzsVXMpIVRbf8048VLGIbomvhhb\nSBUn1vrstjS+01Zy8zgalbTJTX3XzsOiaCLGulvrd6D899lAm+aFq44G/VEGa3Lu\nM7f6tuAGt9iZ7WpgZrzAqL1pJwKBgQDuMEco/9f8NXOSviHHV71GdyED5OMvqv7Y\n/b+MQ2zjxusN2k2GJgmF0ayRcnc36nhw0cUyzAVYxmvvEPV6P+LMRnw7Hsf89O4k\nc8mpDpMloS+HnMH7S8SKG/gS/4QmeDR8k/qsCAEpi6cqtC/olPlTlgy0vXSOGWQQ\nwRupSBVA0wKBgQDPEcAgvUKEvsUkZybYizqn02nWdzncsxY6XnT58eKrR8CgUj+F\nmvgh6h3iS0K3OJpOKplkdZ8mUHRKFi5uoP+TCiKzeWjGrFgLbHBHUhK/j1y6+eYz\n72UiZwmJvJJIokZOMm4KfZ5mGes8oAimWtM17HYdRYGi7l442uAFJDGhVQKBgQC+\ne7d871YQacK6mPk0jVNeFgk+Lv8M8QgMCqn0Bzv+0ObL1khnPuYgsbT7QHpdKlMV\njnzRCd5Ax7Yrovldwdejm77gHNa80jfcyQh9/Zzp3ATBxDhRup87//AdaWCKz1jS\nRBmVGHWtfvS6Lw2dR/44vWf95wFeXqnqyDRR5caxZwKBgQC9weNL9NFD5r7wv/4p\nLaW9NepzATvjZMKxflISHLQDB2h/F2t2tQoGdqUUxo3QN+0xE6lugoYYN4gCP4ik\nnvvc4K/9Wiax712W6C7lFLpwoBXl5E/K1y71NmmGBkeQMKpSjoW+ZgqMEjtfd+HL\nygKdJOjC6tdJpY+cW2i8GRXWjQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "api-260@spreadsheet-352910.iam.gserviceaccount.com",
    "client_id": "110911257756557358222",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/api-260%40spreadsheet-352910.iam.gserviceaccount.com"
}
sa = gspread.service_account_from_dict(Credentials)
def auth():
    uname = platform.uname()
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        # get the GPU id
        gpu_id = gpu.id
        # name of GPU
        gpu_name = gpu.name
    HardwareInfo = ""
    svmem = psutil.virtual_memory()
    try:
        HardwareInfo = f"{uname.system} {uname.node} {uname.release} {uname.processor}{gpu_name}{gpu_id}"
    except:
        HardwareInfo = f"{uname.system} {uname.node} {uname.release} {uname.processor}"
    HWID = HardwareInfo
    HWID = HWID.encode()
    HWID = md5(HWID)
    HWID = HWID.hexdigest()

    username = input("username: ")
    password = input("password: ")
    password = password.encode()
    password = md5(password)
    password = password.hexdigest()
    sh = sa.open("login info")
    wks = sh.worksheet("1")
    usernames = wks.col_values(1)
    passwords = wks.col_values(2)
    hwids = wks.col_values(3)
    if username not in usernames:
        return False 

    meantUserId = usernames.index(username)
    
    if password == passwords[meantUserId] and HWID == hwids[meantUserId]:
        return True
    else:
        return False
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
    print("Made by Headshot56#6069 and helped by the dev team\n")

logo()

def jitter(waittime, jitterV):
    x, y = mouse.get_position()
    time.sleep(waittime)
    mouse.move(x + random.randint(jitterV * -1, jitterV), y + random.randint(jitterV * -1, jitterV))

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

isLoggedIn = auth()

if isLoggedIn != True:
    print(f"Wrong Login info")
    input("Press enter to close. . .")
    exit()
while True:
    os.system("cls")
    logo()
    menu = -69420
    while menu != 1 and menu != 2 and menu != 3:
        try:
            menu = int(input("[1]Clicker\n[2]Settings\n[3]Prefabs\n[>]"))
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
                            if jittering == 1:
                                jitter(wait_time, jitterV)
                                if cbutton == 2:
                                    mouse.click('right')
                                else:
                                    mouse.click()
                            else:
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
                                if jittering == 1:
                                    jitter(wait_time, jitterV)
                                    if cbutton == 2:
                                        mouse.click('right')
                                    else:
                                        mouse.click()
                                else:
                                    time.sleep(wait_time)
                                    if cbutton == 2:
                                        mouse.click('right')
                                    else:
                                        mouse.click()

            elif menu == 2:
                #Settings menu
                try:
                    print("WARNING! Jitter will not work unless you turn off raw_input in your mouse settings in minecraft\nPause the game and click settings --> Controls --> Mouse Settings\nThen turn off raw input\n")
                    toggle = int(input("[1]Toggle\n[2]Press and hold\n[>]"))
                    cbutton = int(input("[1]Left Click\n[2]Right Click\n[>]"))
                    keybind = input("What key would you like to activate your autoclicker: ")
                    print("The fastest time allowed is 0.01 seconds slowest is 9.99. Make sure your upper bound is different than your lower")
                    wait_timeL = float(input("Lower bound of wait time in seconds(ex- 0.01): "))
                    wait_timeL = float(format(wait_timeL, ".2f"))
                    wait_timeU = float(input("Upper bound of wait time in seconds(ex- 9.99): "))
                    wait_timeU = float(format(wait_timeU, ".2f"))
                    jittering = int(input("[1]Jitter (move mouse automatically)\n[2]No jitter\n[>]"))
                    if jittering == 1:
                        jitterV = int(input("We reccomend you set this value very low (1-10) for best results\nEnter a number for pixels to move per jitter: "))
                    else:
                        jitterV = 0
                    input("Settings finished - Press enter to continue. . .")
                except:
                    input("Please input the correct things!")
            elif menu == 3:
                #Prefabs menu
                ly = int(input("[1]Load a prefab\n[2]Save current settings to a prefab\n[>]"))
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
                            jitterV = int(listd[5])
                            input(f"Succesfully loaded config: {filenam}.sun\nPress enter to continue")
                    elif ly == 2:
                        filenam = input("What is the name of the config: ")
                        with open(f"{filenam}.sun", "w+") as file:
                            formatted_data = f"{keybind}-{wait_timeL}-{wait_timeU}-{toggle}-{cbutton}-{jitterV}"
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