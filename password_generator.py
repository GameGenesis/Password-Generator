import os
import string
import secrets
import random

letters = list(string.ascii_letters)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
include_punctuation = True
punctuation = list(string.punctuation)

def generateRandomPassword(length=8):
    password = ""
    for i in range(length):
        password += str(secrets.choice(password_components))
    return password

def generatePasswordFromInput(length=8, inputs=[]):
    password = ""
    random.shuffle(inputs)
    i = 0
    while len(password) < length:
        index = i
        if i < len(inputs):
            for j in range(len(inputs[i])):
                if index < length:
                    password += inputs[i][j]
                    index += 1
        password += str(secrets.choice(password_components))
        i += 1
    
    return password

def generateRandomPIN(length=4):
    password = ""
    for i in range(length):
        password += str(secrets.choice(numbers))
    return password

def generateSecretKey(length=16):
    return secrets.token_urlsafe(length)

def improvePassword(current_password=""):
    password = current_password[:len(current_password)//2]
    password += str(secrets.choice(punctuation))
    password += current_password[len(current_password)//2+1:]
    password += str(secrets.choice(password_components))
    password += str(secrets.choice(numbers))
    return password

def handleError(error_str):
    print(f">> Error: {error_str}")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

while True: #While the program is running, display the command menu and ask the user to enter a command
    password_components = letters + numbers + punctuation
    clearConsole()
    command = input(
    f"""This is a password generator. Enter the number of the command to execute.

_________________________________

 1. Generate Random Password
 2. Generate Password from Input
 3. Generate PIN Number
 4. Generate Secret Key
 5. Improve Existing Password
 6. Toggle Include Punctuation: {include_punctuation}
 7. Exit
_________________________________
> """
    )

    #Check if command is an int; if yes, parse to int
    if (command.isnumeric()):
        command = int(command)

    #Call the function corresponding to the command. If the command is not valid, print an error message.
    if command == 1:
        repeat = "y"

        print("Generate Random Password")
        length = input("Password Length > ")
        if (length.isnumeric()):
            length = int(length)

        while(repeat == "y"):
            print(f">> {generateRandomPassword(length)}")
            repeat = input("\nRepeat: [y/n] > ")
    elif command == 2:
        repeat = "y"

        print("Generate Password From Input")
        length = input("Password Length > ")
        if (length.isnumeric()):
            length = int(length)
        
        num_of_inputs = input("Number of Inputs > ")
        if (num_of_inputs.isnumeric()):
            num_of_inputs = int(num_of_inputs)
        
        inputs = []
        for i in range(num_of_inputs):
            inputs.append(str(input("Inputs > ")))

        while(repeat == "y"):
            print(f">> {generatePasswordFromInput(length, inputs)}")
            repeat = input("\nRepeat: [y/n] > ")
        
    elif command == 3:
        repeat = "y"

        print("Generate PIN Number")
        length = input("PIN Length > ")
        if (length.isnumeric()):
            length = int(length)

        while(repeat == "y"):
            print(f">> {generateRandomPIN(length)}")
            repeat = input("\nRepeat: [y/n] > ")
    elif command == 4:
        repeat = "y"

        print("Generate Secret Key")
        length = input("Key Length > ")
        if (length.isnumeric()):
            length = int(length)

        while(repeat == "y"):
            print(f">> {generateSecretKey(length)}")
            repeat = input("\nRepeat: [y/n] > ")
    elif command == 5:
        repeat = "y"

        print("Improve Existing Password")
        current_password = input("Existing Password > ")

        while(repeat == "y"):
            print(f">> {improvePassword(current_password)}")
            repeat = input("\nRepeat: [y/n] > ")
    elif command == 6:
        include_punctuation = not include_punctuation
        if(include_punctuation):
            punctuation = list(string.punctuation)
        else:
            punctuation = []
    elif command == 7:
        break
    else:
        handleError("Invalid Command.")
        print("_________________________________")
        input()