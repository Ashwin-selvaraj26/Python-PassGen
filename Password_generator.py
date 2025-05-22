import random
import string

def getNumber(prompt) :
    while True:
        num_str = input(prompt)
        if num_str.isdigit():
            return int(num_str)
        else:
            print("Invalid input!")

def yesRno(prompt) :
    while True:
        user_inp = input(prompt).lower()
        if user_inp in ('y', 'n'):
            return user_inp
        else:
            print('invalid input')

def randString(length,useCapital,useNumber,useSpecial):
    characters = string.ascii_lowercase
    if useCapital == 'y':
        characters += string.ascii_uppercase
    if useNumber == 'y':
        characters += string.digits
    if useSpecial == 'y':
        characters += string.punctuation

    random_string = ''.join(random.choices(characters, k=length))
    return random_string


print('---------------------')
print('Password Generator!!!')
print('---------------------')

while True:
    passLength = getNumber("Length: ")
    includeCapital = yesRno("include capital letters? (y/n): ").lower()
    includeNumebers = yesRno("include numbers? (y/n): ").lower()
    specialCharacters = yesRno("include special characters? (y/n): ").lower()

    password = randString(passLength,includeCapital,includeNumebers,specialCharacters)

    print(f"Generated password: {password}")

    userInp = yesRno("generate again? (y/n)")

    if userInp == 'n':
        break



