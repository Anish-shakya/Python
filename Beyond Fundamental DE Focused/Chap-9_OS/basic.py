import os

print(os.getcwd()) # Get the current working directory

print(os.path.abspath(__file__)) # get absolute path of the current file (entire path)

print(os.path.dirname(os.path.abspath(__file__))) # get the directory name of the current file

print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")) # join the file path

print(os.listdir()) # list all files and directories in the current directory

print(os.listdir((os.path.join(os.path.dirname(os.path.abspath(__file__)),"data"))))

for i in os.listdir():
    if os.path.isfile(i):
        print(f"{i} is a file")
    elif os.path.isdir(i):
        print(f"{i} is a directory")
