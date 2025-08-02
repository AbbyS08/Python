# Basic File Operations

import os

def main():
    try:
        # Making the main directory
        os.mkdir("MyFiles")
        # Making three subdirectories
        os.mkdir("MyFiles/Docs")
        os.mkdir("MyFiles/Images")
        os.mkdir("MyFiles/Videos")
    # Error Messages
    except FileExistsError:
        print("A file already exists.")
    except FileNotFoundError:
        print("A file couldn't be found.")
    except:
        print("Something went wrong.")

main()