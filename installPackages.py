import inquirer
import os

package_lists = {
    "Cryptography": ["Cryptool", "Hashcat"],
    "Networking": ["tcpdump", "nmap"],
    "Web": ["dirbuster", "gobuster"],
    "Steganography": ["steghide", "stegsolve"],
    "Exploit Development": ["pwntools", "johntheripper", "metasploit"],
    "OSINT": ["Sherlock", "Recon-ng"],
    "Misc": ["PayloadsAllTheThings", "Seclists", "hydra", "rockyou"]
}

package_commands = {
    "cryptool": "wget https://github.com/jcryptool/core/releases/download/1.0.9/JCrypTool-1.0.9-Linux-64bit.tar.gz && tar -zxvf JCrypTool-1.0.9-Linux-64bit.tar.gz "
    #we also need to edit our ~/.zshrc or ~/.bshrc and add a line of alias jcryptool and execute the jcryptool according to the location of the git-repo
    #we also need to convert this into a multi-line
    "hashcat": "sudo apt install hashcat",
    "tcpdump": "sudo apt install tcpdump",
    "nmap": "sudo apt install nmap",
    "dirbuster": "sudo apt install dirbuster",
    "gobuster": "sudo apt install gobuster",
    # Add more packages and commands here
}

def main():
    selected_packages = {}

    questions = [
        inquirer.Checkbox('packages',
                          message='Choose packages to install(Mark and Unmark with "X"):',
                          choices=list(package_lists.keys()),  # Convert keys to list
                          default=list(package_lists.keys())), # Convert keys to list
    ]
    category_answers = inquirer.prompt(questions)['packages']

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
                print(f"Installing {package}...")
                os.system(install_command)
            else:
                print(f"No installation command found for {package}")

    # Implement installation steps based on the selected categories and packages
    

if __name__ == '__main__':
    main()