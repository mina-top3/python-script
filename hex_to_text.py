#!/usr/bin/python


def again():
    print()
    reply = input("try again [Y / N] ? ")
    if reply == "Y" or reply == "y":
        decrypt()
    else:
        print()
        print("good bye ..")
        print()


def decrypt():
    try:
        print()
        encode = input("enter hex code : ")
        text = bytearray.fromhex(encode).decode()
        print()
        print(text)
    except Exception as ex:
        print()
        print(str(ex))

    again()


decrypt()






