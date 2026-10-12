
import os
import sys

print("Python Version:", sys.version)

print("Current Directory:", os.getcwd())
folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created successfully.")
else:
    print("Directory already exists.")


file_path = os.path.join(folder, "sample.txt")

with open(file_path, "w") as file:
    file.write("Hello! This is a sample file.")

print("File created successfully.")
print("Files and Directories:", os.listdir())


new_path = os.path.join(folder, "new_sample.txt")
os.rename(file_path, new_path)
print("File renamed successfully.")

print("Command-line Arguments:", sys.argv)

os.remove(new_path)
print("File deleted successfully.")

os.rmdir(folder)
print("Directory deleted successfully.")
