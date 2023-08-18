#!/bin/bash

# Choose distribution
echo "Choose your Linux distribution:"
echo "1. Debian-based (Parrot/Kali)"
echo "2. Arch-based"
read -p "Current Distro: " distribution

case $distribution in
    1)
        echo "Debian (Parrot/Kali) OS Customization Script"
        sudo apt-get update
        ;;
    2)
        echo "Arch-based OS Customization Script"
        sudo pacman -Syyu
        ;;
    *)
        echo "Invalid option"
        exit 1
        ;;
esac

#Install Inquirer Python Dependency
pip install inquirer

# Call the Python script
python3 installPackages.py
