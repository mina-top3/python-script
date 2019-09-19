#!/usr/bin/python

try:
    import googlesearch
    from googlesearch import *
except Exception as ex:
    print(str(ex))
    print()
    print("pip3 install google")
    print("pip3 install google-search")
    print("pip3 install beautifulsoup4")

def again():
    print()
    reply = input("try again [Y / N] ? ")
    if reply == "Y" or reply == "y":
        dorking()
    else:
        print()
        print("good bye ..")
        print()


def dorking():
    try:
        print()
        dork = input("enter website dork : ")
        print()
        number = int(input("enter resualt number : "))
        print()
        for item in search(dork, stop=number):
            print(item)
    
    except Exception as exc:
        print()
        print(str(exc))
    again()

dorking()
