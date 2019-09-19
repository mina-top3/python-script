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
        hash = str(input("enter hash : "))
        print()
        hashType = str(input("enter hash type : "))
        print()
        wordlist = input("enter word list : ")
        print()
        wordlist = wordlist.replace("'",'')
        wordlist = wordlist.rstrip()
        list = open(wordlist, 'r')
        list = list.readlines()
        for word in list:
            word = word.replace('\n','')
            startHash = hashlib.new(hashType)
            startHash.update(word.encode("utf-8"))
            endHash = startHash.hexdigest()
            if endHash == hash:
                print("=========> " + word)
                input()
            else:
                print(word)
        list.close()
    except Exception as ex:
        print()
        print(str(ex))
    again()

hashing()
