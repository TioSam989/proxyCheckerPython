import pyperclip
from simple_term_menu import TerminalMenu
from time import sleep
from utils.proxy_validators import (
    validate_proxy,
    format_proxy_to_object,
    filter_active_proxies,
)
from tqdm import tqdm
from utils.proxy_tester import test_http_https_proxy
from utils.proxy_url_operations import handle_list_url
from utils.os_operations import clear_screen
from utils.proxy_file_operations import (
    add_list_proxies_to_file,
    read_proxies_from_file,
    save_successful_proxies,
    add_proxies_to_file,
)

proxy_meh = """
##############################################################
#                                                     _      #
#                                                    | |     #
#  _ __   _ __   ___  __  __ _   _   _ __ ___    ___ | |__   #
# | '_ \ | '__| / _ \ \ \/ /| | | | | '_ ` _ \  / _ \| '_ \  #
# | |_) || |   | (_) | >  < | |_| | | | | | | ||  __/| | | | #
# | .__/ |_|    \___/ /_/\_\ \__, | |_| |_| |_| \___||_| |_| #
# | |                         __/ |                          #
# |_|                        |___/            /TioSam989     #
##############################################################
"""


def app_import_list_url():
    print(proxy_meh)

    urlOut = None
    list = None

    while urlOut is None:
        txtUrl = input("URL (raw.githubusercontent/.../*.txt only): ")
        if txtUrl.endswith(".txt"):
            urlOut = txtUrl
        clear_screen()
        print(proxy_meh)

    options = [
        "⦿ HTTP",
        "⦿ HTTPS",
        "⦿ SOCKS4",
        "⦿ SOCKS5",
    ]
    terminal_menu = TerminalMenu(options, title="\nChoose a protocol:")
    menu_entry_index = terminal_menu.show()

    protocol = ["HTTP", "HTTPS", "SOCKS4", "SOCKS5"][menu_entry_index]
    list = handle_list_url(protocol, urlOut)

    options2 = [
        "⦿ Test proxies from URL",
        "⦿ Import all Proxy list (without any test)",
        "⦿ Exit",
    ]

    terminal_menu2 = TerminalMenu(options2, title="\nChoose an option:")
    if len(list) > 0:
        print(f"Got {len(list)} items on list...")
    menu_entry_index = terminal_menu2.show()
    clear_screen()

    if menu_entry_index == 0:
        print("Running... (This operation can take a few minutes.)")
        try:
            active_proxies = filter_active_proxies(
                list, test_http_https_proxy, format_proxy_to_object, tqdm
            )
            sleep(1)
            clear_screen()
            print(f"Found {len(active_proxies)} active proxies.")

            options3 = [
                "⦿ Save Success proxies",
                "⦿ Copy success proxies",
                "⦿ Exit",
            ]
            terminal_menu = TerminalMenu(options3, title="\nChoose an option:")
            menu_entry_index = terminal_menu.show()

            if menu_entry_index == 0:
                add_list_proxies_to_file(
                    active_proxies, "./proxies.txt", format_proxy_to_object
                )
            elif menu_entry_index == 1:
                pyperclip.copy(str(active_proxies))
            elif menu_entry_index == 2:
                return 0

        except KeyboardInterrupt:
            print("\nProgram interrupted by user.")
    elif menu_entry_index == 1: 
        add_list_proxies_to_file(list, "./proxies.txt", format_proxy_to_object)
        return 0
    elif menu_entry_index == 2:
        return 0


def app_add_proxie():
    cond = True
    while cond:
        clear_screen()
        print(proxy_meh)
        new_proxie = input("Enter Proxy (format: protocol://ip:port): ")
        add_proxies_to_file(new_proxie, "./proxies.txt")
        sleep(1)

        options = [
            "⦿ Add another one",
            "⦿ Exit",
        ]
        terminal_menu = TerminalMenu(options, title="\nOptions:", menu_cursor="> ")
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            cond = True
        elif menu_entry_index == 1:
            print("Exiting...")
            break


def app_test_proxies():
    print(proxy_meh)
    print("Running...")

    proxy_list = read_proxies_from_file("./proxies.txt", validate_proxy)
    successful_proxies = []

    print(f"Testing {len(proxy_list)} proxies...")

    for proxy_type, url, port in proxy_list:
        try:
            success, message, result = test_http_https_proxy(proxy_type, url, port)
            if success:
                successful_proxies.append((proxy_type, url, port))
            print(message)
        except Exception as e:
            print(f"Error testing proxy {url}:{port}: {e}")

    print("Finished...")
    sleep(1)

    while True:
        clear_screen()
        print(proxy_meh)

        options = [
            "⦿ Save Success List",
            "⦿ Copy Success List",
            "⦿ Exit",
        ]
        terminal_menu = TerminalMenu(options, title="\nOptions:", menu_cursor="> ")
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            save_successful_proxies(successful_proxies, "./success_proxies.txt")
            sleep(1)
        elif menu_entry_index == 1:
            pyperclip.copy(str(successful_proxies))
            print("Copied successfully!")
            sleep(1)
        elif menu_entry_index == 2:
            print("Exiting...")
            break


def main():
    while True:
        clear_screen()
        print(proxy_meh)

        options = [
            "⦿ Test file proxies",
            "⦿ Add new proxies to file",
            "⦿ Import proxies from URL (.txt file)",
            "⦿ Exit",
        ]
        terminal_menu = TerminalMenu(options, title="\nOptions:")
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            clear_screen()
            app_test_proxies()
        elif menu_entry_index == 1:
            clear_screen()
            app_add_proxie()
        elif menu_entry_index == 2:
            clear_screen()
            app_import_list_url()
        elif menu_entry_index == 3:
            clear_screen()
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
