import os
import time


def clear_screen():
    time.sleep(1)
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
