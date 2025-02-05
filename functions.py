def my_function():
 print("Hello from a function")
def my_function():
 print("Hello from a function")
my_function() 

def my_function(fname):
 print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus") 

def my_function(fname, lname=""):  # Make `lname` optional with a default value
    print(fname + " " + lname)

# Call the function with both arguments
my_function("Emil", "Refsnes")  # Output: Emil Refsnes

# Call the function with only the first argument
my_function("Emil")  # Output: Emil 

#arbitrary arguments
def my_function(*kids):
 print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") 

def my_function(**kid):
 print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes") 

#default parameter
def my_function(country = "Norway"):
 print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Ireland")

def my_function(x):
 return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))  