def writetodiary(data):
    try:
        file=open(file_name, "a") ## open a file in append mode
    except FileNotFoundError:
        print("Wrong file or file path")

    dt_now = datetime.datetime.now()
    file.write("Date / Time: ")
    file.write((dt_now.strftime("%c")))
    file.write("\n")        
    file.write("Dear Diary: ")
    file.writelines(data)
    file.write("\n" * 2)
    file.close()

def readfromdiary():
    try:
        file=open(file_name, "r") ## open a file in read mode
    except FileNotFoundError:
        print("Wrong file or file path")

    if os.stat(file_name).st_size == 0:
        print("Diary is empty, please add a new entry.")
    else:
        print(file.read())

    file.close()

def erasemydiary():
    try:
        open(file_name, "w").close() ## open a file in read mode
        print("Diary erased.")
    except FileNotFoundError:
        print("Wrong file or file path")

#diary entry
import datetime
import os

file_name = "data.txt"
d_dir = 'C:/Users/vvanden/Documents/Python/Python-Tutorial/Personal Diary'

try:
    os.chdir(d_dir)
except WindowsError:
    print("WindowsError, confirm folder locaiton")
    quit()

d_in = input("Welcome to your diary, would you like to (R)ead, (W)rite, or (E)rase?:")

if d_in == "R" or d_in == "r":
    readfromdiary()
elif d_in == "W" or d_in == "w":
    writetodiary(input("Dear diary:"))
elif d_in == "E" or d_in == "e":
    d_in = input("Are you sure you want to erase the Diary? (Y / N):")
    if d_in == "Y" or d_in == "y":
        erasemydiary()
    else:
        quit()        
else:
    print("InputError, input not recgonized.")
    quit()