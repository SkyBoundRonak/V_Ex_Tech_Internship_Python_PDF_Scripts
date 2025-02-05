#sets are written in curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)  

#duplicates are not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) 

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#length of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#DataTypes
set1 = {"abc", 34, True,40, "Male"}

myset = {"hp", "lenovo","dell" } 
print(type(myset))

#set items cannot chnage , add new items
thisset = {"hp", "lenovo","dell"}
thisset.add("asus")
print(thisset)

thisset = {"hp", "lenovo","dell"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

#Update set 
thisset = {"hp", "lenovo","dell"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove set items
thisset = {"hp", "lenovo","dell"}
thisset.remove("hp")
print(thisset)

#remove item using pop method
thisset = {"hp", "lenovo","dell"}
x = thisset.pop()
print(x)
print(thisset) 

#usng clear in set
thisset = {"hp", "lenovo","dell"}
thisset.clear()
print(thisset) 


#loop set
thisset = {"hp", "lenovo","dell"}
for x in thisset:
 print(x) 
 
#join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 

#join using update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#intersection_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) 


#symmetric_difference_update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#del to delete set completely 
thisset = {"hp", "lenovo","dell"}
del thisset
print(thisset)
