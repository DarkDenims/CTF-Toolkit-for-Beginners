#!/bin/bash

# Output color variables
RED='\033[0;31m'
NC='\033[0m'

# Choose which distro
echo -e "${RED}[*] Choose your Linux distribution:${NC}"
options=("Debian-based (Parrot/Kali)" "Arch-based")

select opt in "${options[@]}"; do
    case $opt in
        "Debian-based (Parrot/Kali)")
            echo -e "${RED}[*] Debian (Parrot/Kali) OS Customization Script${NC}"
            # Update Repositories for Debian-based distro
            echo -e "${RED}[*] Updating repo list${NC}"
            sudo apt-get update
            break
            ;;
        "Arch-based")
            echo -e "${RED}[*] Arch-based OS Customization Script${NC}"
            # Update Repositories for Arch-based distro
            echo -e "${RED}[*] Updating repo list${NC}"
            sudo pacman -Syyu
            break
            ;;
        *)
            echo -e "${RED}Invalid option${NC}"
            ;;
    esac
done