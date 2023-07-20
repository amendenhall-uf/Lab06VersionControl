# Andrew Mendenhall
def encode(password):
    encodedPass = ""
    for i in range(len(password)): # For each item in the password
        encodedPass += str(int(password[i])+3)[-1] # Add the first digit of the number plus 3 to the password
    return encodedPass

def decode(password):
    decodedPass = ""
    for i in range(len(password)):
        decodedPass += str(int(password[i])+7)[-1] # Add the first digit of the number plus 7
        # This first digit is the same as if it were shifted 3 items down
    return decodedPass
if __name__ == "__main__":
    passEncoded = ""
    while True:
        print("Menu\n-------------\n1. Encode \n2. Decode \n3. Quit\n")
        option = int(input())
        if option == 1:
            passEncoded = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        elif option == 2:
            print(f'The encoded password is {passEncoded}, and the original password is {decode(passEncoded)}.')
        elif option == 3:
            break