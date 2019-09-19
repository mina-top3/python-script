#!/usr/bin/python
try:
    import hashlib
except Exception as ex:
    print(str(ex))
    print()
    print("pip3 install hashlib")
    print()

def again():
    print()
    reply = input("try again [Y / N] ? ")
    if reply == "Y" or reply == "y":
        hashing()
    else:
        print()
        print("good bye ..")
        print()


def hashing():
    try:
        print()
        text = input("enter text to hash : ")
        print()
        hashTypes = hashlib.algorithms_available
        print("press enter to view hash types : ")
        input()
        for item in hashTypes:
            print(item)
        print()
        hashType = input("enter hash type : ")
        print()
        startHash = hashlib.new(hashType)
        startHash.update(text.encode("utf-8"))
        endHash = startHash.hexdigest()
        print()
        print(endHash)
        print()
    except Exception as ex:
        print(str(ex))
        print()
    again()

hashing()
