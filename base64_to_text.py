#!/usr/bin/python
try:
    import base64
except Exception as ex:
    print(str(ex))


def again():
    print()
    reply = input("try again [Y / N] ? ")
    if reply == "Y" or reply == "y":
        decoding()
    else:
        print()
        print("good bye ..")
        print()

def decoding():
    try:
        print()
        encode = str(input("enter encode : "))
        text = base64.b64decode(encode).decode('utf-8')
        print()
        print(text)

    except Exception as ex:
        print()
        print(str(ex))
    again()


decoding()