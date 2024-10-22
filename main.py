def encode(password): #encodes password
    encoded_pass = ''
    for i in password:
        encoded_pass += str(int(i) + 3)
    print("Your password has been encoded and stored!")
    return encoded_pass

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
        if option == 1:
            passcode = input("Please enter your password to encode: ")
            passcode = encode(passcode)
        if option == 2:
            pass # decode method
        print()

