import pyperclip
import time
import os

from utils.proxy_tester import test_http_https_proxy
from utils.proxy_file_operations import read_proxies_from_file, save_successful_proxies
from utils.os_operations import clear_screen

def app_test_proxies():
    print("Running...")
    proxy_list = read_proxies_from_file("./proxies.txt")
    successful_proxies = []

    for proxy_type, url, port in proxy_list:
        success, message = test_http_https_proxy(proxy_type, url, port)

        if success:
            successful_proxies.append((proxy_type, url, port))

        print(message)
    print("Finished...")
    time.sleep(1)

    while True:
        clear_screen()
        print("\nMenu2:")
        print("S - Save success proxies")
        print("C - Copy success proxies")
        print("[SPACE] - Skip")

        choiceTwo = input("Enter your choice: ").upper()

        if choiceTwo == "S":
            save_successful_proxies(successful_proxies, "../success_proxies.txt")
            time.sleep(1)

        elif choiceTwo == "C":
            pyperclip.copy(str(successful_proxies))
            print("Copied successfully!")
            time.sleep(1)

def main():
    while True:
        clear_screen()
        print("\nMenu:")
        print("A - Test file proxies")
        print("B - Add new proxies to file (in development)")
        print("C - Exit")

        choice = input("Enter your choice: ").upper()

        if choice == "A":
            clear_screen()
            app_test_proxies()

        elif choice == "B":
            clear_screen()
            print("In development")

        elif choice == "C":
            clear_screen()
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
