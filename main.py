def encoder(password):
    passWord = ''
    for i in password:
        number = int(i)
        if number >= 7:
            newNumber = number -7
        else:
            newNumber = number + 3
        passWord += str(newNumber)
    return  passWord


def main():

    print("Menu")
    print("------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = input("Please enter an option: ")
    password1 = input("Please enter your password to encode:")


def decode(password):
    result = ''
    for i in password:
        num = int(i)
        if num >= 7:
            new_num = num + 7
        else:
            new_num = num - 3
        result += new_num
    return result
