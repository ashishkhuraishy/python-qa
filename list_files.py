import os

#  entering the path to directory
dir_path = input("please enter the path to dir  : ")

# listing out all the files in that directory
files = os.listdir(dir_path)

# looping thorugh each item in that files
for file in files:
    # checking if the files have these extensions
    if file.endswith(".pdf") or file.endswith(".png"):
        # printing the files with valid extensions
        print(file)