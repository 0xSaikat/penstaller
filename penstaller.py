#!/usr/bin/env python3
import subprocess
import time
import sys
import os
from termcolor import colored
from pyfiglet import Figlet


def slow_print(text, color=None, delay=0.05):
    for char in text:
        sys.stdout.write(colored(char, color) if color else char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_box(text, color="cyan"):
    border = "═" * (len(text) + 4)
    slow_print(f"╔{border}╗", color)
    slow_print(f"║  {text}  ║", color)
    slow_print(f"╚{border}╝", color)


def print_banner():
    os.system("clear")  
    banner = """╭─────[By 0xSaikat]─────────────────────────────────────────────╮
│                                                               │
│     ____                  __        ____                      │
│    / __ \___  ____  _____/ /_____ _/ / /__  _____             │
│   / /_/ / _ \/ __ \/ ___/ __/ __ `/ / / _ \/ ___/             │
│  / ____/  __/ / / (__  ) /_/ /_/ / / /  __/ /                 │
│ /_/    \___/_/ /_/____/\__/\__,_/_/_/\___/_/  v-1.0           │
│                                                               │
╰──────────────────────────────────────────[hackbit.org]────────╯"""
    slow_print(banner, "green")


def check_admin_privileges():
    try:
        result = subprocess.run(['id', '-u'], capture_output=True, text=True)
        return result.stdout.strip() == '0'
    except Exception:
        return False


def get_admin_privileges():
    if check_admin_privileges():
        return True
    
    slow_print("[!] Administrative privileges are required to install the tools.", "yellow")
    slow_print("[!] Please enter your password when prompted.", "yellow")
    
    try:
        subprocess.run(['sudo', 'echo', "Administrative privileges confirmed."], check=True)
        return True
    except subprocess.CalledProcessError:
        slow_print("[!] Failed to obtain administrative privileges.", "red")
        return False


def run_command(command, shell=False):
    try:
        if shell:
            subprocess.run(command, shell=True, check=True)
        else:
            subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def install_package(pkg):
    slow_print(f"[!] {pkg} is not installed. Preparing to install...", "yellow")
    start_time = time.time()

    try:
        if pkg == "unzip":
            subprocess.run(["sudo", "apt-get", "install", "-y", "unzip"], check=True)
        elif pkg == "wget":
            subprocess.run(["sudo", "apt-get", "install", "-y", "wget"], check=True)
        elif pkg == "go":
            subprocess.run(["sudo", "apt-get", "install", "-y", "golang"], check=True)
        elif pkg == "cmake":
            subprocess.run(["sudo", "apt-get", "install", "-y", "cmake"], check=True)
        elif pkg == "pip":
            subprocess.run(["sudo", "apt-get", "install", "-y", "python3-pip"], check=True)
        elif pkg == "cargo":
            subprocess.run(["sudo", "apt-get", "install", "-y", "cargo"], check=True)
        elif pkg == "ruby":
            subprocess.run(["sudo", "apt-get", "install", "-y", "ruby-rubygems"], check=True)
        else:
            slow_print(f"[!] Unsupported package: {pkg}", "red")
            return False

        elapsed_time = time.time() - start_time
        slow_print(f"[*] {pkg} installed in {elapsed_time:.2f} seconds", "green")
        return True
    except subprocess.CalledProcessError:
        slow_print(f"[!] Unable to install {pkg}, please try manually", "red")
        return False


def install_tool(tool):
    slow_print(f"[!] {tool} is not installed. Preparing to install...", "yellow")
    start_time = time.time()

    try:
        if tool == "xsstrike":
            success = run_command(["pip3", "install", "xsstrike"])
        elif tool == "dalfox":
            success = run_command("wget https://github.com/hahwul/dalfox/releases/download/v2.9.2/dalfox_2.9.2_linux_amd64.tar.gz && tar xvf dalfox_2.9.2_linux_amd64.tar.gz && sudo mv dalfox /usr/bin/ && rm -rf dalfox_2.9.2_linux_amd64.tar.gz README.md LICENSE.txt", shell=True)
        elif tool == "pdsi":
            success = run_command(["go", "install", "github.com/1hehaq/pdsi@latest"])
        elif tool == "ghauri":
            success = run_command("git clone https://github.com/r0oth3x49/ghauri.git && cd ghauri && pip3 install -r requirements.txt && python3 setup.py install && cd .. && rm -rf ghauri", shell=True)
        elif tool == "feroxbuster":
            success = run_command("wget https://github.com/epi052/feroxbuster/releases/latest/download/feroxbuster_amd64_linux.zip && unzip feroxbuster_amd64_linux.zip && sudo mv feroxbuster /usr/bin/ && rm -f feroxbuster_amd64_linux.zip", shell=True)
        elif tool == "shhgit":
            success = run_command("go install github.com/eth0izzle/shhgit@latest && sudo mv $(go env GOPATH)/bin/shhgit /usr/bin/", shell=True)
        elif tool == "jaeles":
            success = run_command("go install github.com/jaeles-project/jaeles@latest && sudo mv $(go env GOPATH)/bin/jaeles /usr/bin/", shell=True)
        elif tool == "crlfuzz":
            success = run_command("go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest && sudo mv $(go env GOPATH)/bin/crlfuzz /usr/bin/", shell=True)
        elif tool == "unfurl":
            success = run_command("go install github.com/tomnomnom/unfurl@latest && sudo mv $(go env GOPATH)/bin/unfurl /usr/bin/", shell=True)
        elif tool == "graphqlmap":
            success = run_command("git clone https://github.com/swisskyrepo/GraphQLmap && cd GraphQLmap && pip3 install -r requirements.txt && sudo ln -sf $(pwd)/graphqlmap.py /usr/bin/graphqlmap && cd ..", shell=True)
        elif tool == "kxss":
            success = run_command("go install github.com/Emoe/kxss@latest && sudo mv $(go env GOPATH)/bin/kxss /usr/bin/", shell=True)
        elif tool == "ssrf-sheriff":
            success = run_command("go install github.com/teknogeek/ssrf-sheriff@latest && sudo mv $(go env GOPATH)/bin/ssrf-sheriff /usr/bin/", shell=True)
        elif tool == "smuggler":
            success = run_command("git clone https://github.com/defparam/smuggler.git && cd smuggler && sudo ln -sf $(pwd)/smuggler.py /usr/bin/smuggler && cd ..", shell=True)
        elif tool in ["hakrawler", "nikto", "nmap", "dirsearch", "amass", "sublist3r", "assetfinder", "nuclei", "massdns", "sqlmap"]:
            success = run_command(["sudo", "apt-get", "install", "-y", tool])
        elif tool in ["xnLinkFinder", "cors", "uro", "arjun"]:
            success = run_command(["pip3", "install", tool])
        elif tool == "wpscan":
            success = run_command(["gem", "install", "wpscan"])
        elif tool == "puredns":
            success = run_command("wget https://github.com/d3mondev/puredns/releases/download/v2.1.1/puredns-Linux-amd64.tgz && tar xvf puredns-Linux-amd64.tgz && sudo mv puredns /usr/bin/ && rm -rf puredns-Linux-amd64.tgz", shell=True)
        elif tool == "httprobe":
            success = run_command("wget https://github.com/tomnomnom/httprobe/releases/download/v0.2/httprobe-linux-amd64-0.2.tgz && tar xvf httprobe-linux-amd64-0.2.tgz && sudo mv httprobe /usr/bin/ && rm -rf httprobe-linux-amd64-0.2.tgz", shell=True)
        elif tool == "subfinder":
            success = run_command("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && sudo mv $(go env GOPATH)/bin/subfinder /usr/bin/", shell=True)
        else:
            
            success = run_command(f"go install -v github.com/projectdiscovery/{tool}/cmd/{tool}@latest && sudo mv $(go env GOPATH)/bin/{tool} /usr/bin/ 2>/dev/null", shell=True)

        if success:
            elapsed_time = time.time() - start_time
            slow_print(f"[*] {tool} installed in {elapsed_time:.2f} seconds", "green")
            return True
        else:
            slow_print(f"[!] Unable to install {tool}, please try manually", "red")
            return False

    except Exception as e:
        slow_print(f"[!] Error installing {tool}: {str(e)}", "red")
        return False


def is_installed(command):
    return subprocess.run(["which", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0


def display_summary(successful_installs, failed_installs):
    print("\n")
    print_box("Installation Summary", "cyan")
    if successful_installs:
        slow_print("[*] Successfully Installed Tools:", "green")
        for tool in successful_installs:
            slow_print(f"  - {tool}", "green")
    if failed_installs:
        slow_print("[!] Failed to Install Tools:", "red")
        for tool in failed_installs:
            slow_print(f"  - {tool}", "red")


def main():
    print_banner()
    
    
    slow_print("[*] Checking for administrative privileges...", "yellow")
    if not get_admin_privileges():
        slow_print("[!] This script requires administrative privileges to install tools.", "red")
        slow_print("[!] Please run the script again with sudo or as root.", "red")
        return

    
    packages = ["unzip", "wget", "go", "cmake", "pip", "cargo", "ruby"]
    successful_installs = []
    failed_installs = []

    for pkg in packages:
        if not is_installed(pkg):
            if install_package(pkg):
                successful_installs.append(pkg)
            else:
                failed_installs.append(pkg)
        else:
            slow_print(f"[^] {pkg} is already installed in your system!", "blue")

    
    tools = ["xsstrike", "dalfox", "puredns", "httprobe", "naabu", "hakrawler", "gospider", 
             "LinkFinder", "SecretFinder", "subjs", "xnLinkFinder", "cors", "gobuster", "nikto",
             "wpscan", "jq", "x8", "urldedupe", "qsreplace", "gau", "gf", "waybackurls", "uro",
             "ffuf", "anew", "subfinder", "httpx", "nmap", "dirsearch", "amass", "sublist3r",
             "assetfinder", "nuclei", "massdns", "shuffledns", "paramspider", "arjun", "katana",
             "sqlmap", "ghauri", "pdsi",
             
             "feroxbuster", "shhgit", "jaeles", "crlfuzz", "unfurl", "graphqlmap", "kxss",
             "ssrf-sheriff", "smuggler", "dnsx", "interactsh", "notify", "asnmap", "tlsx",
             "uncover", "mapcidr", "alterx", "dsieve"]

    for tool in tools:
        if not is_installed(tool):
            if install_tool(tool):
                successful_installs.append(tool)
            else:
                failed_installs.append(tool)
        else:
            slow_print(f"[^] {tool} is already installed in your system!", "blue")

    
    display_summary(successful_installs, failed_installs)

    
    print("\n")
    print_box("Thank you for using Penstaller!", "green")
    slow_print("Happy Hacking! 🚀", "cyan")

if __name__ == "__main__":
    main()
