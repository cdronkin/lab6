# Cole Ronkin Group 44

def encode(password): #encodes password
    encoded_pass = ''
    for i in password:
        encoded_pass += str(int(i) + 3)
    print("Your password has been encoded and stored!")
    return encoded_pass

def decode(encoded_password): # decode method - added by Alisha Chowdhury
    decoded_password = ""
    for digit in encoded_password:
        new_digit = (int(digit) - 3)  # shifting the numbers down by 3
        decoded_password += str(new_digit)  # recreating the decoded password
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
    return decoded_password

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

if __name__ == '__main__':
    option = 0
    passcode = ''
    while option != 3:
        print_menu()
        print()
        option = int(input("Please enter an option: "))
        try:
            if option == 1:
                passcode = input("Please enter your password to encode: ")
                if len(passcode) != 8 or not passcode.isdigit(): #checks length of password and contents to be digit
                    raise ValueError('Invalid Password')
                passcode = encode(passcode)
            elif option == 2:
                # decode method
                decode(passcode)
                pass
        except ValueError as excpt:
            print(excpt)
        print()

