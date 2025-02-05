x = "awesome"
def myfunc():
 print("Python is " + x)
myfunc()
x = "awesome"
def myfunc():
 x = "fantastic"
 print("Python is " + x)
myfunc()
print("Python is " + x)
def myfunc():
 global x
 x = "fantastic"
myfunc()
print("Python is " + x) 


x = "awesome"          # Global variable
def myfunc():
    print("Python is " + x)  # Uses the global variable
myfunc()               # Output: Python is awesome

x = "awesome"          # Global variable remains "awesome"
def myfunc():
    x = "fantastic"    # Local variable
    print("Python is " + x)  # Uses the local variable
myfunc()               # Output: Python is fantastic
print("Python is " + x) # Global variable remains "awesome"
                       # Output: Python is awesome

def myfunc():
    global x           # Modify the global variable
    x = "fantastic"    # Change global variable to "fantastic"
myfunc()
print("Python is " + x) # Global variable is now "fantastic"
                       # Output: Python is fantastic
