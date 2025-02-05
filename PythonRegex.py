import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  
#Set of characters [a-m]
import re

txt1 = "The rain in Spain"


#finding all lower case characters

x = re.findall("[a-m]", txt)
print(x)




