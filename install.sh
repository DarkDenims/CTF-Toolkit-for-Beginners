#!/bin/bash

# Choose distribution
echo "Choose your Linux distribution:"
read -p "1. Debian-based (Parrot/Kali), 2. Arch-based: " distribution

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

# Call the Python script
python3 install_packages.py
