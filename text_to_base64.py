#!/usr/bin/python
try:
    import base64
except Exception as ex:
    print(str(ex))


def again():
    print()
    reply = input("try again [Y / N] ? ")
    if reply == "Y" or reply == "y":
        encoding()
    else:
        print()
        print("good bye ..")
        print()

def encoding():
    try:
        print()
        text = str(input("enter text : "))
        encode = base64.b64encode(text.encode('utf-8'))
        print()
        print(encode)

    except Exception as ex:
        print()
        print(str(ex))
    again()


encoding()