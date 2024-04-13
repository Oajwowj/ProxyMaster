import socket
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pycountry
import time
import os
import sys
import argparse

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

print(f"{RB}Creator: B1te")
print(f"{Y}Team: Bl4ckB1t Team")
print(f"{B}Telegram: https://t.me/+jgf9WGttQMY5NmY8")
print(f"{PU}Github: https://github.com/Bl4ckB1t")

# OPTION NUMBER 1

def PROXY_service(num_proxies=10, save_to_file=False, filename=None):
    a_six = 1
    b_six = 2
    
    output_text = ""

    while a_six < b_six:
        a_six += 1

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
                output_text += "  Number  |   IP Address    |    Port      |   Anonymity   |   HTTPS   |   Last Checked |      Country\n"
                output_text += "__________|_________________|______________|_______________|___________|________________|___________________________\n"
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

                if save_to_file and filename:
                    save_proxies_to_file(df['IP Address'].tolist(), filename)

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


def MAIN_FUNC_TEST_SAVE(filename="proxies.txt", timeout=3):

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

        timeout = int(timeout)

        socket.setdefaulttimeout(timeout)

        print(RB)

        os.system("clear")
        
        print("\nTEST PROXY BY ProxyMaster TOOL")

        print("-------------------------------\n")

        with open(filename, "r") as file:

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

        active_file_name = input(f"\n{Y}Enter file name to store {G}active proxies{Y} (Press Enter To Skip) {RB}#{WB} ")

        if active_file_name == "":

            pass

        else:

            with open(active_file_name, "w") as active_file:

                active_file.write("\n".join(active_proxies))

        inactive_file_name = input(f"{Y}Enter file name to store {RB}inactive proxies{Y} (Press Enter To Skip) {RB}#{WB} ")

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

############################################

def count_lines(text):
    lines = text.split('\n')
    return len(lines)

############################################

def main():
    print(WB)
    parser = argparse.ArgumentParser(description="Proxy Tool")
    parser.add_argument("option", type=int, choices=[1, 2, 3], help="Select an option: 1 - Get Proxies, 2 - Save Proxies In File, 3 - Test Proxy")
    parser.add_argument("--num_proxies", type=int, default=300, help="Number of proxies to retrieve (default: 300) - Only for option 1 and 2")
    parser.add_argument("--filename", type=str, help="File path to save proxies (for option 2) or file path containing proxies to test (for option 3)")
    parser.add_argument("--timeout", type=int, default=10, help="Timeout for testing proxies (default: 3) - Only for option 3")
    args = parser.parse_args()

    if args.option == 1:
        PROXY_service(args.num_proxies)
    elif args.option == 2:
        if args.filename:
            save_proxy_ips_to_file(args.filename, args.num_proxies)
        else:
            print("Filename is required for option 2")
    elif args.option == 3:
        if args.filename:
            MAIN_FUNC_TEST_SAVE(args.filename, args.timeout)
        else:
            print("Filename is required for option 3")

if __name__ == "__main__":
    main()
