# File open
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "r")
print(f.read())

# Read first 5 characters
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "r")
print(f.read(5))

# Read lines
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "r")
print(f.readline())
print(f.readline())

# Close the file
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "r")
print(f.readline())
f.close()

# File write (append)
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "a")
f.write("Now the file has more content!")
f.close()

# Open and read the file after appending
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "r")
print(f.read())

# File write (overwrite)
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# Open and read the file after overwriting
f = open(r"C:\Users\ronak\Downloads\SEM8 Internship\Cyber Notes.txt", "r")
print(f.read())

# Create a new file
f = open("myfile.txt", "w")
f.write("This is some content.")
f.close()

# Append to the new file
f = open("myfile.txt", "a")
f.write("\nThis is additional content.")
f.close()

# Delete file
import os

file_name = "myfile.txt"

if not os.path.exists(file_name):
    f = open(file_name, "x")
    f.write("This is some content.")
    f.close()
else:
    print(f"The file '{file_name}' already exists.")

# Exception handling
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")