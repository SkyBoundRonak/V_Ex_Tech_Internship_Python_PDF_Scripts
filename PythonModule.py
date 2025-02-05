import mymodule
mymodule.greeting("Ronak")

import mymodule
a = mymodule.person1["age"]
print(a) 

import mymodule as mx
a = mx.person1["age"]
print(a) 

import platform
x = platform.system()
print(x) 


import platform
x = dir(platform)
print(x) 


#Import only the person1 dictionary from the module:
from mymodule import person1
print (person1["age"]) 


import datetime
x = datetime.datetime.now()
print(x)
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A")) 