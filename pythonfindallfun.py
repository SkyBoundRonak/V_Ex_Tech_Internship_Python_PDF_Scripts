import re

txt = "The rain in Spain"

#Check if "ireland the string:

x = re.findall("Ireland",txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
  
  
#search function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

#split function
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#sub function()
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)