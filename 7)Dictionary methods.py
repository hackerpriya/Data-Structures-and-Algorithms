person = {
    "name": "John Doe",
    "age": 30,
    "gender": "Male",
    "city": "New York",
    "address": "123 Main Street"
}

# Methods to manipulate dictionaries

# 1. copy() method: Creates a copy of the original dictionary.
person2 = person.copy()
print("1. Copy of the dictionary using copy() method:", person2)
print()

# 2. fromkeys() method: Creates a new dictionary from a given sequence of elements with a value provided by the user.
newDict = {}.fromkeys([1,2,3])
print("2. New dictionary from keys [1, 2, 3] using fromkeys() method:", newDict)
newDict2 = {}.fromkeys([1,2,3],["Kui","Pui","Chui"])
print("3. New dictionary from keys [1, 2, 3] with default value using fromkeys() method:", newDict2)
newDict3 = {}.fromkeys([1,2,3],"Kuchi")
print("4. New dictionary from keys [1, 2, 3] with default value 'Kuchi' using fromkeys() method:", newDict3)
print()

# 3. get(key, value) method: Returns the value of a specified key.
print("5. Value of 'name' key using get() method:", person.get("name"))
print("6. Value of 'name' key with default value 'Priyanka' using get() method:", person.get("name", "Priyanka"))
print("7. Value of 'ID' key with default value 100 using get() method:", person.get("ID", 100))
print("8. Value of 'ID' key using get() method:", person.get("ID"))
print()

# 4. items() method: Returns a list of dictionaries as tuple pairs.
print("9. List of key-value pairs using items() method:", person.items())
print()

# 5. keys() method: Returns a view object displaying a list of all keys in the dictionary.
print("10. List of keys using keys() method:", person.keys())
print()

# 6. popitem() method: Deletes and returns the last key-value pair of the dictionary.
print("11. Last deleted key-value pair using popitem() method:", person.popitem())
print("12. Dictionary after deleting the last key-value pair using popitem() method:", person)
print()

# 7. setdefault() method: Returns the value of a key present in the dictionary.
print("13. Value of existing key 'name' with default value 'Priyanka' using setdefault() method:", person.setdefault("name", "Priyanka"))
print("14. Dictionary after setdefault() with existing key using setdefault() method:", person)
print("15. Value of new key 'name1' with default value 'Priyanka' using setdefault() method:", person.setdefault("name1", "Priyanka"))
print("16. Dictionary after setdefault() with new key using setdefault() method:", person)
print()

# 8. pop() method
print("17. Using pop() with a key that exists but with a value as 'not' using pop() method:", person.pop("name", "not"))
print("18. Dictionary after using pop() with a key that exists using pop() method:", person)
print("19. Using pop() with a key that exists and its real value using pop() method:", person.pop("name", "John Doe"))
print("20. Dictionary after using pop() with a key that does not exist using pop() method:", person.pop("name2", "not"))
print()

# 9. values() method: Returns a view object displaying a list of values in the dictionary.
print("21. List of values using values() method:", person.values())
print()

# 10. update() method: Updates a dictionary with elements from another dictionary.
person3 = {
    "name": "Alice Johnson",
    "age": 35,
    "gender": "Female",
    "city": "Chicago",
    "email": "alice@example.com"
}

person4 = {
    "fullname": "Michael Brown",
    "age": 45,
    "gender": "Male",
    "city": "Houston",
    "phone": "+1 (555) 987-6543"
}

person3.update(person4)
print("22. Updated dictionary using update() method:", person3)
print()

# 11. clear() method: Deletes all elements from the dictionary.
person.clear()
print("23. Dictionary after clear() method:", person)
