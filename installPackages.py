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
    "Misc": ["SecLists", "hydra", "WordLists"]
}

# Define your package commands for both Debian and Arch
package_commands_debian = {
    # Debian package commands
    "Cryptool": (
        "wget https://github.com/jcryptool/core/releases/download/1.0.9/JCrypTool-1.0.9-Linux-64bit.tar.gz && "
        "tar -zxvf JCrypTool-1.0.9-Linux-64bit.tar.gz && "
        "cd {home_dir}/JCrypTool-1.0.9-Linux-64bit && "
        "echo 'alias jcryptool=\"$(which jcryptool)\"' >> {rc_file}"
    ),
    "Hashcat": "sudo apt-get install hashcat -y",
    "tcpdump": "sudo apt-get install tcpdump -y",
    "nmap": "sudo apt-get install nmap -y",
    "dirbuster": "sudo apt-get install dirbuster -y",
    "gobuster": "sudo apt-get install gobuster -y",
    "steghide": "sudo apt-get install steghide -y",
    "stegsolve": (
        "$ wget http://www.caesum.com/handbook/Stegsolve.jar -O ~/stegsolve.jar &&"
        "chmod +x ~/stegsolve.jar &&"
        "echo 'alias stegsolve=\"java -jar ~/stegsolve.jar\"' >> {rc_file}"
    ),
    "pwntools": "pip install pwntools",
    "johntheripper": "sudo apt-get install john -y",
    "metasploit": (
        "sudo apt install curl gpgv2 autoconf bison build-essential git-core libapr1 postgresql libaprutil1 libcurl4-openssl-dev libgmp3-dev libpcap-dev openssl libpq-dev libreadline6-dev libsqlite3-dev libssl-dev locate libsvn1 libtool libxml2 libxml2-dev libxslt-dev wget libyaml-dev ncurses-dev  postgresql-contrib xsel zlib1g zlib1g-dev &&"
        # yes, I know. It's Long
        # That's what she said.
        # But these are dependencies of Metasploit.
        "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall &&"
        "chmod 755 msfinstall &&"
        "./msfinstall"
    ),
    "Sherlock": "sudo apt-get install sherlock -y",
    "Recon-ng": "sudo apt-get install recon-ng -y",
    "SecLists": "sudo apt-get install seclists -y",
    "hydra": "sudo apt-get install hydra -y",
    "WordLists": "sudo apt-get install wordlists -y"
}

package_commands_arch = {
    # Arch package commands
    "Cryptool": (
        "wget https://github.com/jcryptool/core/releases/download/1.0.9/JCrypTool-1.0.9-Linux-64bit.tar.gz && "
        "tar -zxvf JCrypTool-1.0.9-Linux-64bit.tar.gz && "
        "cd {home_dir}/JCrypTool-1.0.9-Linux-64bit && "
        "echo 'alias jcryptool=\"$(which jcryptool)\"' >> {rc_file}"
    ),
    "Hashcat": "sudo pacman -S hashcat --noconfirm",
    "tcpdump": "sudo pacman -S tcpdump --noconfirm",
    "nmap": "sudo pacman -S nmap --noconfirm",
    "dirbuster": "sudo pacman -S dirbuster --noconfirm",
    "gobuster": "sudo pacman -S gobuster --noconfirm",
    "steghide": "sudo pacman -S steghide --noconfirm",
    "stegsolve": (
        "$ wget http://www.caesum.com/handbook/Stegsolve.jar -O ~/stegsolve.jar &&"
        "chmod +x ~/stegsolve.jar &&"
        "echo 'alias stegsolve=\"java -jar ~/stegsolve.jar\"' >> {rc_file}"
    ),
    "pwntools": "pip install pwntools",
    "johntheripper": "sudo pacman -S john --noconfirm",
    "metasploit": (
        "sudo pacman -S metasploit --noconfirm"
        # Add additional commands for setting up Metasploit on Arch if needed
    ),
    "Sherlock": "sudo pacman -S sherlock --noconfirm",
    "Recon-ng": "sudo pacman -S recon-ng --noconfirm",
    "SecLists": "sudo pacman -S seclists --noconfirm",
    "hydra": "sudo pacman -S hydra --noconfirm",
    "WordLists": "sudo pacman -S wordlists --noconfirm"
}

home_dir = os.path.expanduser("~")
rc_file = os.path.expanduser("~/.zshrc")  # or "~/.bashrc" depending on the user's shell
package_commands_debian = {pkg: cmd.format(home_dir=home_dir, rc_file=rc_file) for pkg, cmd in package_commands_debian.items()}
package_commands_arch = {pkg: cmd.format(home_dir=home_dir, rc_file=rc_file) for pkg, cmd in package_commands_arch.items()}

def main():
    selected_packages = {}

    questions = [
        inquirer.Checkbox('packages',
                          message='Choose packages to install(Mark and Unmark with "X"):',
                          choices=list(package_lists.keys()),  # Convert keys to list
                          default=list(package_lists.keys())), # Convert keys to list
    ]
    category_answers = inquirer.prompt(questions)['packages']

    # Ask which distribution the user is using
    distro_question = [
        inquirer.List('distro',
                      message='Which distribution are you using?',
                      choices=['Debian', 'Arch'],
                      default='Debian'),
    ]
    distro_answer = inquirer.prompt(distro_question)['distro']

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
            if distro_answer == 'Debian':
                install_command = package_commands_debian.get(package)
            elif distro_answer == 'Arch':
                install_command = package_commands_arch.get(package)
            else:
                install_command = None

            if install_command:
                rc_file = "~/.zshrc" if shell_answer == 'Zsh' else "~/.bashrc"
                formatted_install_command = install_command.format(rc_file=rc_file)

                print(f"Installing {package}...")
                print(f"Running command: {formatted_install_command}")
                os.system(formatted_install_command)
                print(f"{package} installed.")
            else:
                print(f"No installation command found for {package}")

if __name__ == '__main__':
    main()
    print("\nPackage installation completed.")
