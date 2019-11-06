# Program that finds all files in a folder with specified extensions that then duplictes the files and stores them in a new folder

# Import statements
import glob
import os
import sys
import shutil

# Function that opens a file named extensions and reads the necessary extensions in list order
def readFromFile():
    try:
        f = open("extensions.txt","r")
        temp_list = f.read().splitlines()
        extension_list = [e.replace(' ', '') for e in temp_list]
        return extension_list
    except IOError as e:
        print("The following error occurred while reading the file: %s" %e)
        sys.exit(1)

# Function that recursively finds all files with the neccessary extensions, prints them to console, and creates a list of the files
def printFiles(var_extensions):
    complete_list = []
    for e in var_extensions:
        files = glob.glob(r"\Users\Armanya Dalmia\PycharmProjects\DirectoryBrowser" + '/**/*.'+e, recursive=True)
        complete_list.extend(files)
        for f in files:
            print("C:" + f)
    if not len(complete_list) == 0:
        return complete_list
    else:
        print("There are no files with the matching extension(s) in this directory")
        sys.exit(1)

# Function that creates a folder for the files to be moved, checks for duplication, and moves the file if there are no duplicates
def moveFiles(file_list):
    current_directory = os.getcwd()
    destination = os.path.join(current_directory, r'testTransfer')
    if not os.path.exists(destination):
        os.makedirs(destination)
    if len(os.listdir(r"\Users\Armanya Dalmia\PycharmProjects\DirectoryBrowser\testTransfer")) > 0:
        for f in file_list:
            if os.path.isfile(r"\Users\Armanya Dalmia\PycharmProjects\DirectoryBrowser\testTransfer" + "\\" + os.path.basename(f)):
                continue
            else:
                shutil.copy2(f, r"\Users\Armanya Dalmia\PycharmProjects\DirectoryBrowser\testTransfer")
    else:
        for f in file_list:
            shutil.copy2(f, r"\Users\Armanya Dalmia\PycharmProjects\DirectoryBrowser\testTransfer")

# Runs all functions to actually create the program
extensions = readFromFile()
print(extensions)
fileList = printFiles(extensions)
moveFiles(fileList)
