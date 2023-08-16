# Using Linux?

If you're already inside a Linux environment or planning to run a linux environment via WSL feel free to follow these steps to install most of these tools.
1. Clone this repo
```
git clone https://github.com/DarkDenims/CTF-Toolkit-for-Beginners.git
```
2. Move to the directory and run the install.sh file
```
sudo ./install.sh
```
3. Select which type of distro your linux environment is under, and choose which software to install.


# Tools sorted by Category
## Cryptography

| Tool        | Description                                                 | Where to Get It | Used on      |
|-------------|-------------------------------------------------------------|-----------------|--------------|
| Cryptool    | Versatile tool for understanding and using encryption methods. Crack encryptions, unlock hidden messages, and solve cryptographic puzzles. | [Download](https://www.cryptool.org/en/ct1/downloadslink) | Windows, Linux |
| Hashcat     | Powerful password cracking tool. Crack hashed passwords, reveal hidden secrets, and find vulnerabilities. | [Download](https://hashcat.net/hashcat/) | Windows, Linux |

## Networking

| Tool        | Description                                                 | Where to Get It | Used on      |
|-------------|-------------------------------------------------------------|-----------------|--------------|
| tcpdump     | Command-line packet analyzer for capturing and analyzing network traffic. Peek at conversations and patterns to solve CTF challenges. | Available in Debian and Arch-based package managers | Linux |
| nmap        | Powerful network discovery and auditing tool. Scan networks, reveal vulnerable ports, and identify vulnerabilities. | [Download](https://nmap.org/download.html) | Windows, Linux |


## Web Exploitation

| Tool        | Description                                                 | Where to Get It | Used on      |
|-------------|-------------------------------------------------------------|-----------------|--------------|
| Burp Suite  | Comprehensive web vulnerability scanner and proxy. Identify vulnerabilities, fix security loopholes. | [Download](https://portswigger.net/burp/communitydownload) | Windows, Linux |
| OWASP Zap   | Spot security issues and protect websites from threats. | [Download](https://www.zaproxy.org/download/) | Windows, Linux |
| Postman     | Interact with APIs. Send requests, receive responses for API-related tasks in CTF challenges. | [Download](https://www.postman.com/downloads/) | Windows, Linux |
| DirBuster   | Web application security tool for brute-forcing directories and files. Identify hidden content in web servers. | [GitHub](https://gitlab.com/kalilinux/packages/dirbuster/-/tree/kali/master) | Linux |
| Gobuster    | Tool for directory and file brute-forcing in web application testing. | [GitHub](https://github.com/OJ/gobuster) | Windows, Linux |

## Steganography

| Tool        | Description                                                 | Where to Get It | Used on      |
|-------------|-------------------------------------------------------------|-----------------|--------------|
| Steghide    | Command-line tool for hiding data within images and sounds. Reveal concealed info, solve steganography puzzles. | [Download](https://sourceforge.net/projects/steghide/) | Windows, Linux |
| stegsolve   | Graphical tool for visual steganography analysis. Unveil hidden content in images for image-based CTF challenges. | [Download](https://wiki.bi0s.in/steganography/stegsolve/) | Windows, Linux |

## Forensics

| Tool        | Description                                                 | Where to Get It | Used on      |
|-------------|-------------------------------------------------------------|-----------------|--------------|
| Autopsy     | Open-source digital forensics platform. Analyze digital evidence, dissect artifacts, and analyze data trails. | [Download](https://www.autopsy.com/download/) | Windows, Linux |

## Exploit Development

| Tool        | Description                                                 | Where to Get It | Used on      |
|-------------|-------------------------------------------------------------|-----------------|--------------|
| Pwntools    | CTF framework and exploit development library. Craft exploits, solve puzzles, create sophisticated hacks on Linux-based systems. | [Documentation](https://docs.pwntools.com/en/latest/install.html) | Linux |
| John the Ripper | Password cracking tool. Test password combinations to breach security barriers and expose weaknesses. | [Download](https://www.openwall.com/john/) | Windows, Linux |
| Metasploit  | Versatile framework for exploit development. Identify and exploit vulnerabilities, essential for hacking and system infiltration in CTF tasks. | [Download](https://www.metasploit.com) | Windows, Linux |

## Miscellaneous

Aside from these tools, there are also some miscellaneous tools you might need to use in solving CTF challenges or explore on your own:

| Tool        | Description                                                 | Where to Get It | Platform     |
|-------------|-------------------------------------------------------------|-----------------|--------------|
| PayloadsAllTheThings | A GitHub repo providing a comprehensive collection of payloads, encoders, fuzzing payloads, web shells, and more. | [GitHub](https://github.com/swisskyrepo/PayloadsAllTheThings) | Windows, Linux |
| SecLists    | Another GitHub repo with a collection of security-related lists including wordlists, fuzzing lists, and more. | [GitHub](https://github.com/danielmiessler/SecLists) | Windows, Linux |
| Exploit Database | A website listing known exploits and vulnerabilities maintained by Offensive Security. | [ExploitDB](https://www.exploit-db.com/) | Windows, Linux |
| Hydra       | Fast and flexible password-cracking tool supporting multiple protocols and services. | Included with Kali Linux, [GitHub](https://github.com/vanhauser-thc/thc-hydra) | Windows, Linux |
| rockyou     | Popular wordlist containing commonly used passwords. Ideal for password cracking. | Included with Kali Linux, [GitHub](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) | Windows, Linux |