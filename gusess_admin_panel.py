#!/usr/bin/python
try:
    import urllib
    from urllib import request
except Exception as ex:
    print(str(ex))
    print()
    print("pip3 install urllib5")

def again():
    print()
    reply = input("try again [Y / N] ? ")
    if reply == "Y" or reply == "y":
        gusess()
    else:
        print()
        print("good bye ..")
        print()


def gusess():
    try:
        print()
        site = input("enter website to gusess : ")
        print()
        wordList = input("enter word list : ")
        print()
        wordList = wordList.replace("'",'')
        wordList = wordList.rstrip()
        list = open(wordList, 'r')
        cleanList = list.readlines()
        for item in cleanList:
            link = "https://www." + site +"/"+ item
            try:
                urllib.request.urlopen(link)
                print("=========> " + link)
                input()
            except:
                print(link)
        list.close()
    except Exception as ex:
        print()
        print(str(ex))
    again()

gusess()
