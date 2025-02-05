#simple pattern print
rows = 5
for i in range(rows):
 for j in range(i+1):
  print("* ", end="")
 print("\n")
 
#back pattern print
 n = 5
for i in range(0, n):
 for j in range(n-i):
  print("*", end=" ")
 print() 

#printing number pattern
rows = 5
for i in range(rows):
 for j in range(i+1):
  print(j+1, end=" ")
 print("\n")
 
#printing star with -1
rows = 5
for i in range(rows, 0, -1):
 for j in range(0, i):
  print("* ", end=" ")
 print("\n")

#printing numbers from 5to1 
# Number of rows in the pattern
rows = 5

# Loop to print the pattern
for i in range(rows, 0, -1):
    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")

    print()

#printing patterns with space

# Number of rows in the pattern
rows = 5

# Loop to print the pattern
for i in range(rows, 0, -1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    # Move to the next line
    print()
 
a = 8
for i in range(0, 5):
 for j in range(0, a):
  print(end=" ")
 a = a - 2
 for j in range(0, i+1):
  print("* ", end="")
 print()



# Number of rows in the pyramid
n = 5

# Loop through each row
for i in range(1, n + 1):
    # Print leading spaces (to center the asterisks)
    for j in range(n - i):
        print(" ", end="")
    
    # Print asterisks
    for k in range(i):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()