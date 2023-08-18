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

    # Implement installation steps based on the selected categories and packages

if __name__ == '__main__':
    main()
c