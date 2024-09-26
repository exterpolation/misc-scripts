import pyautogui as gui
import time
import os

usr = os.getlogin()


def spam() -> None:
    limit = input("Quanti messaggi vuoi scrivere?: ").strip()
    if not limit.isnumeric() or limit == "0":
        print("Il limite deve essere un numero maggiore di 0!\n")
        return

    message = input("E il Messaggio che vuoi scrivere?: ").strip()
    if limit == "" or message == "":
        print("Non puoi lasciare uno o piu' dei campi vuoti!")
        return

    time.sleep(2)

    for _ in range(int(limit)):
        gui.typewrite(message)
        gui.press("enter")

    print(f"\nMessaggi scritti: {limit}\nMessaggio scritto: '{message}'\n")


def setup_console() -> None:
    os.system("clear")
    os.system("mode con: cols=145 lines=50")


if __name__ == "__main__":
    setup_console()

    print("""
     /$$                           /$$          /$$               /$$$$$$
    | $$                          |__/         | $/              /$$__  $$
    | $$        /$$$$$$  /$$   /$$ /$$  /$$$$$$|_//$$$$$$$      | $$  \\__/  /$$$$$$   /$$$$$$  /$$$$$$/$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$
    | $$       /$$__  $$|  $$ /$$/| $$ |____  $$ /$$_____/      |  $$$$$$  /$$__  $$ |____  $$| $$_  $$_  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$
    | $$      | $$$$$$$$ \\  $$$$/ | $$  /$$$$$$$|  $$$$$$        \\____  $$| $$  \\ $$  /$$$$$$$| $$ \\ $$ \\ $$| $$ \\ $$ \\ $$| $$$$$$$$| $$  \\__/
    | $$      | $$_____/  >$$  $$ | $$ /$$__  $$ \\____  $$       /$$  \\ $$| $$  | $$ /$$__  $$| $$ | $$ | $$| $$ | $$ | $$| $$_____/| $$
    | $$$$$$$$|  $$$$$$$ /$$/\\  $$| $$|  $$$$$$$ /$$$$$$$/      |  $$$$$$/| $$$$$$$/|  $$$$$$$| $$ | $$ | $$| $$ | $$ | $$|  $$$$$$$| $$
    |________/ \\_______/|__/  \\__/|__/ \\_______/|_______/        \\______/ | $$____/  \\_______/|__/ |__/ |__/|__/ |__/ |__/ \\_______/|__/
                                                                          | $$
                                                                          | $$
                                                                          |__/
    """)

    print(f"\nBenvenuto sullo Spammer di Lexia, {usr}! (Reminder: hai due secondi per cliccare sulla box in "
          f"cui vuoi scrivere)")

    while True:
        spam()

        if input("Vuoi continuare? (Y/n):").lower()[0] not in ['y', 's']:
            print(f"Arrivederci, {usr}! ")
            break
