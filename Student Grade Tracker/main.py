def averagedata():
    try:
        file=open(file_name, "r") ## open a file in read mode
    except FileNotFoundError:
        print("Wrong file or file path")

    if os.stat(file_name).st_size == 0:
        print("File is empty, please confirm file locaiton")
    else:
        # Open the CSV file
        with open(file_name, 'r') as file:
            # Create a CSV reader
            csv_reader = csv.reader(file)
    
            # Read the header row
            header = next(csv_reader)
    
            # Initialize lists to store names and averages
            names = []
            averages = []

            # Iterate through each row
            for row in csv_reader:
                # Extract names
                lname, fname = row[:2]
                full_name = f"{fname} {lname}"
                names.append(full_name)

                # Convert the row values to integers
                row_values = [int(value) for value in row[2:]]  # Skipping the first two columns (LName and FName)
        
                # Calculate the average and append to the list
                row_average = sum(row_values) / len(row_values)
                row_average = round(row_average, 1)
                averages.append(row_average)

        # Display the names and averages
        for name, average in zip(names, averages):
            print(f"{name}: Average = {average}")

        file.close()

def erasedata():
    try:
        open(file_name, "w").close() ## open a file in read mode
    except FileNotFoundError:
        print("Wrong file or file path")

def inputdata():
    try:
        file=open(file_name, "a") ## open a file in append mode
    except FileNotFoundError:
        print("Wrong file or file path")
    for i in range(data_len):
        print("Input:" + data_ls[i])
        if (cat_ls[i] == "str"):
            item = str(input())
            data_out = item
        elif (cat_ls[i] == "int"):
            item = int(input())
            if (item > 100) or (item < 0):
                print("error, value must be between 0 and 100")
                data_out = "0"
            else:
                data_out = str(item)
        else:
            "Data error: incorrect data catatory configured"
        file.write(data_out)
        if i < (data_len - 1): #no comma required at the end of the data set
            file.write(",")
        else:
            file.write("\n")
    file.close()

def formathead():
    try:
        file=open(file_name, "a") ## open a file in append mode
    except FileNotFoundError:
        print("Wrong file or file path")
    for i in range(data_len):
        file.write(data_ls[i])
        if i < (data_len - 1): #no comma required at the end of the data set
            file.write(",")
        else:
            file.write("\n")
    file.close() 

#diary entry
import os
import csv

file_name = "data.csv"
dir = 'C:/Users/vvanden/Documents/Python/Python-Tutorial/Student Grade Tracker'

try:
    os.chdir(dir)
except WindowsError:
    print("WindowsError, confirm folder locaiton")
    quit()

req = input("Student Grade Tracker, would you like to add (G)rades, display (A)varage, (I)nitialize year:")

cat_ls = ['str', 'str', 'int', 'int', 'int', 'int', 'int', 'int', 'int']
data_ls = ['First_Name', 'Last_Name', 'Language', 'Math', 'French', 'Science', 'SocialStudies', 'Health', 'Art']
data_len = len(data_ls)

if req == "G" or req == "g":
    inputdata()
elif req == "A" or req == "a":
    averagedata()
elif req == "I" or req == "i":
    erasedata()
    formathead()
    print("Data initialized for year")
else:
    print("InputError, input not recgonized.")
    quit()
