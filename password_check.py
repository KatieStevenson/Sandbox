'''
Creates a basic password checking program.
'''

min_length = 8


# Asks user for password and then sends the password off to a function of be validated.
def main():
    print("Please create a password with a minimum of 8 characters: ")
    password = input("> ")
    return valid_char_length(password)


# Checks password fulfills minimum length and prompts user if invalid length.
def valid_char_length(password):
    char_length = (len(password))
    if min_length > char_length:
        print("The password you have entered is invalid")
        return main()
    else:
        return convert_to_asterisks(password)


# Converts each character in password into an asterisks and then displays it to the user.
def convert_to_asterisks(password):
    print("Your password is: ")
    for char in password:
        print(char.replace(char, '*'), end = '')


main()