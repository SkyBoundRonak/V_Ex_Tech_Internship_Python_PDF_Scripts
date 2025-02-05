try:
    print(x)
except:
    print("an exception occurres")
    
try:
    print("Hello,Ronak here")
except:
    print("something when wrong")
else:
    print("nothing went wrong")
    
    
#User input
username = input("Enter username:")
print("Username is: " + username)

#add two number
number1 = input("First number: ")
number2 = input("\nSecond number: ")

# Adding two numbers
sum = int(number1) + int(number2)

# Display the sum
print("The sum of {0} and {1} is {2}" .format(number1,number2, sum)) 