# new_list = [new_item for item in list if condition]

#Make new_list from prev_list only if element is positive number.
prev_list = [-1,10,-20,2,-90,60,45,20]
new_list = [number for number in prev_list if number > 0]
print("List of positive numbers from prev_list : ",new_list)
print()

#Print if a number is Positive number else print "Negative Number" within new_list.
new_list = [number if number>0 else "Negative Number" for number in prev_list]
print("Direct if else statement within list comprehension : ",new_list)
print()

#Print if a number is Positive number else print "Negative Number" within new_list.
def positive_num(number):
    if number>0:
        return number
    else:
        return "Negative Number"
new_list = [positive_num(number) for number in prev_list]
print("Function calling within list comprehension : ",new_list)
print()

#Make new_list from prev_list only if element is square of negative number.
prev_list = [-1,10,-20,2,-90,60,45,20]
new_list = [number**2 for number in prev_list if number < 0]
print("List of square of negative numbers from prev_list : ",new_list)
print()


#Inside if condition,call another function.
#Print list of letters in Sentence with consonants only using function in list comprehension.
sentence = "My name is priyanka"
#Function to check consonants.
def is_consonants(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels
consonants = [letter for letter in sentence if is_consonants(letter)]
print("Print consonants of sentence using function within list comprehension : ",consonants)
print()
    


