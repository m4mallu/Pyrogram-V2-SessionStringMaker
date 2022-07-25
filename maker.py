import os
import pyfiglet
from time import sleep
from pyrogram import Client
from datetime import datetime
from requests.exceptions import ConnectionError

# Clean up os
try:
    os.remove("my.session")
except Exception:
    pass
try:
    os.remove("bot.session")
except Exception:
    pass


# Clean Screen
def clear():
    if os.name == "posix":  # Unix/Linux/MacOS/BSD/etc
        os.system("clear")
    elif os.name == "nt":   # Windows
        os.system("cls")
    else:
        pass


# Start fn
def start():
    clear()
    initial_screen()


#Info Screen
def initial_screen():
    banner = pyfiglet.figlet_format("m4mallu")
    print(banner)
    print("You need to register to get app_id and api_hash in here:\nhttps://my.telegram.org/apps")
    print("\nProject source:\nhttps://github.com/m4mallu/Pyrogram-V2-SessionStringMaker")
    input("\nPress 'Enter' key to continue >>>")
    fill_api()


# Fill the user credentials
def fill_api():
    clear()
    while True:
        api_id = input("Insert app_id: ")
        if str(api_id).isdigit():
            break
        clear()
        print("Invalid app_id!")
        sleep(2)
        clear()

    app_hash = input("Insert api_hash: ")
    if app_hash:
        create_session(api_id, app_hash)


#Session creation
def create_session(api_id, app_hash):
    app = Client(":memory:", api_id, app_hash)
    try:
        clear()
        app.start()
    except Exception:
        clear()
        input("Invalid Id/Hash !\nPress 'Enter' key to continue >>>")
        fill_api()
    except ConnectionError:
        clear()
        input("Network Error! Please try again later.\nPress 'Enter' key to continue >>>")
        fill_api()
    session = app.export_session_string()
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        Client.send_message(self=app,
                            chat_id='me',
                            text=str(f'<b>Session created on: </b>{dt_string}\n\n<code>{session}</code>\n\n'
                                     f'⚠️<b> keep this code confidential</b> ⚠\n\n<b>Credits: '
                                     f'</b>https://github.com/m4mallu'),
                            disable_web_page_preview=True,
                            )
    except Exception:
        print("Error saving session to saved messages\n\n")
        pass
    clear()
    print(f"Done! Your session string is:\n\n{session}")
    print("\n\n1. A copy of session string has been send to your >>Saved Messages<<\n2. Save this session string to a "
          "file and use it in your bot.\nCredits: https://github.com/m4mallu")
    input("\nPress 'Enter' key for main menu >>>")
    app.stop()
    loop()


# Main loop
def loop():
    clear()
    print(pyfiglet.figlet_format("Coded by", font="digital"))
    print(pyfiglet.figlet_format("m4mallu", font="banner3-D"))
    sleep(3)
    clear()
    x = input("Enter 1 to continue\n\nEnter 2 to exit\n\n>>>")
    if x == "1":
        start()
    elif x == "2":
        exit()
    else:
        clear()
        print("Invalid input!")
        sleep(2)
        clear()
        loop()


clear()
loop()
