#Create list from string.
#Strings is a sequence of characters and a list is sequence of values, but a list of characters is not same string.


#Convert a string to a list character using list() function.
a = 'adiyogini'
b = list(a)
print("List of string adiyogini using list() function : ",b)
print()

#Break string into words using split() method.
a = "Adiyogini Adiyogini Adiyogini"
b = a.split()
print("List of string of words using split() method : ",b)
print()

#Break string of words into list of words using split() method.
a = "Adiyogini-Adiyogini-Adiyogini"
b = a.split("-")
print("List of string of words separated with character(-) using split() method : ",b)
print()

#Convert list into string using join() method.
print("String of List elements separated with character(-) using join() method : ","-".join(b))
print()
