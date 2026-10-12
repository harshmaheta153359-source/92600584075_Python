
import os
import shutil


os.makedirs("Source", exist_ok=True)
os.makedirs("Destination", exist_ok=True)


with open("Source/sample.txt", "w") as file:
    file.write("Hello! This is a sample file.")

print("File created successfully.")


shutil.copy("Source/sample.txt", "Destination/sample.txt")
print("File copied successfully.")

shutil.move("Destination/sample.txt", "Source/sample.txt")
print("File moved successfully.")


os.remove("Source/sample.txt")
print("File deleted successfully.")

os.rmdir("Source")
os.rmdir("Destination")
print("Directories deleted successfully.")
