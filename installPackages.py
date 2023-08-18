import inquirer

package_lists = {
    "Cryptography": ["Cryptool", "Hashcat"],
    "Networking": ["tcpdump", "nmap"],
    "Web": ["dirbuster", "gobuster"],
    "Steganography": ["steghide", "stegsolve"],
    "Exploit Development": ["pwntools", "johntheripper", "metasploit"],
    "OSINT": ["Sherlock", "Recon-ng"],
    "Misc": ["PayloadsAllTheThings", "Seclists", "hydra", "rockyou"]
}

def main():
    selected_packages = {}

    for category, packages in package_lists.items():
        questions = [
            inquirer.Checkbox('packages',
                              message=f'Choose packages for {category}',
                              choices=['All'] + packages,
                              default=['All']),
        ]
        answers = inquirer.prompt(questions)
        selected_packages[category] = answers['packages']

    print("Selected packages:")
    for category, packages in selected_packages.items():
        print(f"{category}: {', '.join(packages)}")

    # Implement installation steps based on the selected categories and packages

if __name__ == '__main__':
    main()
