a = [1,2,3]
b = [4,5,6,7]


# Two operations in List
# + operator : Concatenate List
c = a + b
print("Concatenation of a and b lists : ",a+b)
print()

# * operator : Repeat Elements of same list
a = [0,1]
a = a * 4
print("Multiplication operation on list a : ",a)
print()

# Built-in Functions in List
# len()
print("Length of list c using len() function : ",len(c))
print()

# max()
print("Maximum value in list c using max() function : ",max(c))
print()

# min()
print("Minimum value in list c using min() function : ",min(c))
print()

# sum()
print("Sum of all elements in list c using sum() function : ",sum(c))
print()

#Average of List Elements
#Average of Elements can be calculated by combining sum() and len() functions.
average = sum(c)//len(c)
print("Average of elements in list c : ",average)
print()

#Take numbers from the user and find average of those numbers.
print("Take numbers from the user and find average of those numbers.")
total = 0 
count = 0
while True:
    inp = input("Enter a number : ")
    if inp == "Done":
        break
    value = int(inp)
    total += value
    count += 1
    average = total//count
print("Average of all numbers entered by user : ",average)
print()


#Form a list by taking numbers from the user and find average of those numbers by using built-in functions.
print("Form a list by taking numbers from the user and find average of those numbers by using built-in functions.")
numbers = []
while True:
    inp = input("Enter a number : ")
    if inp == "Done":
        break
    value = int(inp)
    numbers.append(value)
    average = sum(numbers)//len(numbers)
print("Average of all numbers within list formed by user input values : ",average)
print()