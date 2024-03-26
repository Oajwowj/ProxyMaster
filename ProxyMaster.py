try:
    import socket
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import pycountry
    import time
    import os
    import sys

    os.system("clear")

    RE = "\033[0m"  # Default
    BL = "\033[38;2;0;0;0m"  # black
    G = "\033[92m"  # green
    Y = "\033[93m"  # yellow
    B = "\033[94m"  # blue
    CY = "\033[46m"  # cyan
    W = "\033[47m"  # white
    PU = "\033[35m"  # purple
    RB = "\033[1;31m"  # red bold
    GUL = "\033[32;4m"  # green under line
    WB = "\033[1;37m"  # white bold

    print(RB)
    print("""
 ____                      __  __           _
|  _ \ _ __ _____  ___   _|  \/  | __ _ ___| |_ ___ _ __
| |_) | '__/ _ \ \/ / | | | |\/| |/ _` / __| __/ _ \ '__|
|  __/| | | (_) >  <| |_| | |  | | (_| \__ \ ||  __/ |
|_|   |_|  \___/_/\_ \\__, |_|  |_|\__,_|___/\__\___|_|V4.0
                    |___/
    """)

    # MAIN INFO

    def slow_typing(line):
        for char in line:
            print(char, end='', flush=True)
            if char in ['\n', '\r']:
                continue
            time.sleep(0.050)

    slow_typing(f"{RB}Creator: B1te\n")
    slow_typing(f"{Y}Team: Bl4ckB1t Team\n")
    slow_typing(f"{B}Telegram: https://t.me/+jgf9WGttQMY5NmY8\n")
    slow_typing(f"{PU}Github: https://github.com/Bl4ckB1t\n")

    # OPTION NUMBER 1

    def PROXY_service(num_proxies=10):
        a_six = 1
        b_six = 2
        output_text = ""

        while a_six < b_six:
            a_six += 1
            output_text += PU + "\n"
            output_text += "The Proxys From : https://free-proxy-list.net/\n"
            output_text += B + "\n"

            try:

                url = "https://free-proxy-list.net/"
                response = requests.get(url)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    tables = soup.find_all('table')

                    proxy_table = tables[0]

                    headers = ['IP Address', 'Port', 'Anonymity', 'Https', 'Last Checked', 'Country']
                    rows = proxy_table.find_all('tr')[1:]

                    proxy_data = []
                    for row in rows:
                        columns = row.find_all('td')
                        ip = columns[0].text.strip()
                        port = columns[1].text.strip()
                        country_code = columns[2].text.strip()
                        anonymity = columns[4].text.strip()
                        https = columns[6].text.strip()
                        last_checked = columns[7].text.strip()

                        try:
                            country = pycountry.countries.get(alpha_2=country_code)
                            country_name = country.name if country else "Unknown"
                        except Exception as e:
                            country_name = "Unknown"

                        proxy_data.append([ip, port, anonymity, https, last_checked, country_name])

                    df = pd.DataFrame(proxy_data, columns=headers)

                    output_text += RB + "\n"
                    output_text += "____________________________________________________________________________________________________________________\n"
                    output_text += "  Number   |   IP Address   |    Port    |   Anonymity   |   HTTPS   |   Last Checked |      Country\n"
                    output_text += "___________|________________|____________|_______________|___________|________________|_____________________________\n"
                    output_text += G + "\n"

                    num_proxies = min(num_proxies, len(df))
                    for index, row in df.head(num_proxies).iterrows():
                        output_text += (
                            str(index + 1).ljust(10) + "|" + row['IP Address'].ljust(15) + "  |" +
                            row['Port'].ljust(12) + "  |" + row['Anonymity'].ljust(14) + " |" +
                            row['Https'].ljust(9) + "  |" + row['Last Checked'].ljust(15) + " |" + row[
                                'Country'] + "\n"
                        )
                    output_text += RB + "__________|_________________|______________|_______________|___________|________________|______________________\n"

                else:
                    output_text += RB + "\n"
                    output_text += "[-] Please Try Again\n"
            except requests.exceptions.ConnectionError:
                output_text += RB + "\n"
                output_text += "[-] No Internet Connection\n"

        line_count = count_lines(output_text)
        print(output_text)

    ############################################

    # OPTION NUMBER 2

    lines_count = 0


    def MAIN_FUNC_TEST_SAVE(num_proxies=300):

        def test_proxy(ip, port):

            global lines_count
            
            lines_count += 1

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:

                s.connect((ip, port))

                print(WB, end="")

                print(
                    f"{G}[+] {WB}Proxy {Y}{ip}:{port}{B}".ljust(72), f"Status: Active{RE}".ljust(40),WB, "Number: ", lines_count)

                return True

            except socket.timeout:

                print(WB, end="")

                print(
                    f"{RB}[-] {WB}Proxy {Y}{ip}:{port}{RB}".ljust(76), f"Status: Timeout{RE}".ljust(40),WB, "Number: ", lines_count)

                return False

            except ConnectionRefusedError:

                print(WB, end="")

                print(f"{RB}[-] {WB}Proxy {Y}{ip}:{port}{RB}".ljust(76), f"Status: Connection Refused{RE}".ljust(40),WB, "Number: ", lines_count)

                return False

            except Exception as e:

                print(WB, end="")

                print(
                    f"{RB}[-] {WB}Proxy {Y}{ip}:{port}{RB}".ljust(76), f"{e}{RE}".ljust(40),WB, "Number: ", lines_count)

                return False

            finally:

                s.close()

        try:
            active_proxies = []

            inactive_proxies = []

            file_name = input(f"\n{B}Enter the file path {RB}#{WB} ")

            timeout = int(input(f"\n{G}Enter The Timeout (In Seconds) {RB}#{WB} "))

            socket.setdefaulttimeout(timeout)

            print(RB)

            print("\nTEST PROXY BY ProxyMaster TOOL")

            print("-------------------------------\n")

            with open(file_name, "r") as file:

                for line in file:

                    ip, port = line.strip().split(":")

                    if test_proxy(ip, int(port)):

                        active_proxies.append(f"{ip}:{port}")
                    else:

                        inactive_proxies.append(f"{ip}:{port}")

            print(WB)

            print(f"{G}Active Proxies: {len(active_proxies)}")

            print(f"{RB}Inactive Proxies: {len(inactive_proxies)}{RE}")

            print(WB)

            active_file_name = input(f"\n{Y}Enter file name to store active proxies (Press Enter To Skip) {RB}#{WB} ")

            if active_file_name == "":

                pass

            else:

                with open(active_file_name, "w") as active_file:

                    active_file.write("\n".join(active_proxies))

            inactive_file_name = input(
                f"{Y}Enter file name to store inactive proxies (Press Enter To Skip) {RB}#{WB} ")

            if inactive_file_name == "":

                pass

            else:
                with open(inactive_file_name, "w") as inactive_file:

                    inactive_file.write("\n".join(inactive_proxies))

        except FileNotFoundError:

            print(f"{RB}[-] File not found. Please provide a valid file path{RE}")

        except ValueError:

            print(f"{RB}[-] Invalid port number. Please check the format of your file{RE}")

        except Exception as e:

            print(f"{RB}[-] An error occurred: {e}{RE}")

    ############################################

    def save_proxies_to_file(proxies, filename):
        with open(filename, 'w') as file:
            for proxy in proxies:
                file.write(proxy + '\n')

    ############################################

    def save_proxy_ips_to_file(FILENAME, num_proxies=300):
        try:
            url = "https://free-proxy-list.net/"
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                tables = soup.find_all('table')
                proxy_table = tables[0]
                rows = proxy_table.find_all('tr')[1:]

                try:
                    with open(FILENAME, 'w') as file:
                        for row in rows[:num_proxies]:
                            columns = row.find_all('td')
                            ip = columns[0].text.strip()
                            port = columns[1].text.strip()
                            file.write(f"{ip}:{port}\n")
                except FileNotFoundError:
                    exit(f"{RB}[-] File Not Found")

            else:
                print(f"{RB}[-] Please Try Again")
        except requests.exceptions.ConnectionError:
            print("[-] No Internet Connection")
        print(f"{G}[+] The Operation Completed")

    while True:

        print(WB, """
[1] Get Proxies
[2] Save Proxies In File
[3] Test Proxy
[4] Exit""")

        print(RB)
        test_or_proxy_or_save = input(f"Select One Of The Options #{WB} ")
        if test_or_proxy_or_save == "1":
            def count_lines(text):
                lines = text.split('\n')
                return len(lines)

            print(B)
            num_proxies = int(input(f"How Many Proxies #{WB} "))
            if num_proxies > 300:
                print(f"{RB}[-] The Maximum Is 300")
                pass
            PROXY_service(num_proxies)

        if test_or_proxy_or_save == "2":
            print(B)

            FILENAME = input(f"Enter The File Path #{WB} ")

            num_proxies_to_store = input(f"{PU}Enter the number of proxies to store (Default 300) #{WB} ")

            if not num_proxies_to_store:

                num_proxies_to_store = 300

            if int(num_proxies_to_store) > 300:

                print(f"{RB}[-] The Maximum is 300")

            num_proxies_to_store = int(num_proxies_to_store)

            save_proxy_ips_to_file(FILENAME, num_proxies_to_store)

        if test_or_proxy_or_save == "3":
            try:

                MAIN_FUNC_TEST_SAVE()

            except Exception as error:
                print(f"{RB}[-] An error occurred: {error}")

        if test_or_proxy_or_save == "4":
            sys.exit()
except Exception as error:
    sys.exit(f"{RB}[-] {error}")
