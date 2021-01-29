import os


while True:
    file = open("example.txt","a")
    word = input("Enter Text :\n")
    file.write(word)
    file.write("\n")
    file.close()
