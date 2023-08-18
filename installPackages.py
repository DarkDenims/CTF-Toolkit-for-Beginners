import inquirer
import os

# Define your package lists
package_lists = {
    "Cryptography": ["Cryptool", "Hashcat"],
    "Networking": ["tcpdump", "nmap"],
    "Web": ["dirbuster", "gobuster"],
    "Steganography": ["steghide", "stegsolve"],
    "Exploit Development": ["pwntools", "johntheripper", "metasploit"],
    "OSINT": ["Sherlock", "Recon-ng"],
    "Misc": ["Seclists", "hydra", "WordLists"]
}

# Define your package commands
package_commands = {
    "cryptool": (
        "wget https://github.com/jcryptool/core/releases/download/1.0.9/JCrypTool-1.0.9-Linux-64bit.tar.gz && "
        "tar -zxvf JCrypTool-1.0.9-Linux-64bit.tar.gz && "
        "cd {home_dir}/JCrypTool-1.0.9-Linux-64bit && "
        "echo 'alias jcryptool=\"$(which jcryptool)\"' >> {rc_file}"
    ),
    "hashcat": "sudo apt install hashcat",
    "tcpdump": "sudo apt install tcpdump",
    "nmap": "sudo apt install nmap",
    "dirbuster": "sudo apt install dirbuster",
    "gobuster": "sudo apt install gobuster",
    "steghide": "sudo apt install steghide",
    "stegsolve": (
        "$ wget http://www.caesum.com/handbook/Stegsolve.jar -O ~/stegsolve.jar &&"
        "chmod +x ~/stegsolve.jar &&"
        "echo 'alias stegsolve=\"java -jar ~/stegsolve.jar\"' >> {rc_file}"
    ),
    "pwntools": "pip install pwntools",
    "johntheripper": "sudo apt-get install john",
    "metasploit": (
        "sudo apt install curl gpgv2 autoconf bison build-essential git-core libapr1 postgresql libaprutil1 libcurl4-openssl-dev libgmp3-dev libpcap-dev openssl libpq-dev libreadline6-dev libsqlite3-dev libssl-dev locate libsvn1 libtool libxml2 libxml2-dev libxslt-dev wget libyaml-dev ncurses-dev  postgresql-contrib xsel zlib1g zlib1g-dev &&"
        "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \"
        "chmod 755 msfinstall && \"
        "./msfinstall"
    ),
    "sherlock": "sudo apt install sherlock",
    "recon-ng": "sudo apt install recon-ng",
    "seclists": "sudo apt install seclists",
    "hydra": "sudo apt install hydra",
    "wordlist": "sudo apt install wordlists"
    
    
}

home_dir = os.path.expanduser("~")
rc_file = os.path.expanduser("~/.zshrc")  # or "~/.bashrc" depending on the user's shell
package_commands = {pkg: cmd.format(home_dir=home_dir, rc_file=rc_file) for pkg, cmd in package_commands.items()}

def main():
    selected_packages = {}

    questions = [
        inquirer.Checkbox('packages',
                          message='Choose packages to install(Mark and Unmark with "X"):',
                          choices=list(package_lists.keys()),  # Convert keys to list
                          default=list(package_lists.keys())), # Convert keys to list
    ]
    category_answers = inquirer.prompt(questions)['packages']

    # Ask which shell the user is using
    shell_question = [
        inquirer.List('shell',
                      message='Which shell are you using?',
                      choices=['Bash', 'Zsh'],
                      default='Bash'),
    ]
    shell_answer = inquirer.prompt(shell_question)['shell']

    for category in category_answers:
        sub_questions = [
            inquirer.Checkbox(f'category_{category}',
                              message=f'Choose packages for {category}',
                              choices=package_lists[category],
                              default=['All']),
        ]
        sub_answers = inquirer.prompt(sub_questions)[f'category_{category}']
        if 'All' in sub_answers:
            selected_packages[category] = package_lists[category]
        else:
            selected_packages[category] = sub_answers

    print("Selected packages:")
    for category, packages in selected_packages.items():
        print(f"{category}: {', '.join(packages)}")
        
        for package in packages:
            install_command = package_commands.get(package)
            if install_command:
                rc_file = "~/.zshrc" if shell_answer == 'Zsh' else "~/.bashrc"
                formatted_install_command = install_command.format(rc_file=rc_file)
                
                print(f"Installing {package}...")
                os.system(formatted_install_command)
            else:
                print(f"No installation command found for {package}")

if __name__ == '__main__':
    main()
