# Define a dictionary with key-value pairs.
myDict = {
    "Miller": "A person who owns or works in a corn mill.",
    "Programmer": "A person who writes computer programs"
}

# Print the dictionary.
print(myDict)

# Access values using keys.
print(myDict["Miller"])
print(myDict["Programmer"])

# Comparison between arrays/lists and dictionaries:

# Array/List:
# If we have an array or list, to access the first element, we need to use an index.
# Example:
# myArray = ["Miller", "Programmer", "App Miller"]
# print(myArray[0])

# Dictionary:
# In a dictionary, values are organized using keys and values pairs.
# To access a value, we retrieve it using the associated key.
# Example:
# myDict = {"Miller": "A person who owns or works in a corn mill.","Programmer": "A person who writes computer programs"}
# print(myDict["Miller"])

# Real-life example: a job at a local cinema cloakroom.
# Each coat is associated with a ticket number.
# Equivalent of an array where ticket number shows the indexes and the coat shows the value.

# If a customer loses their ticket number, we use a different way of organizing the cloakroom.
# Write customer’s name on the ticket and hang the coat, putting their name on it.
# This is equivalent to a dictionary where the name is the key and the coat is the value.

# Example:
# You got a job at a local cinema in a cloakroom.
# To organize the cloakroom efficiently, coats are hung sequentially.
# As new customers come in, you hang the coats on the next available coat hanger and give them a ticket.
# Once the film is over, customers come back looking for their coats. As long as they give you the ticket number, you can identify the coat number and give them their coat back.
# If a customer loses their ticket number, you write their name on the ticket and hang the coat, putting their name on it.

# The dictionary is like writing the customer’s name on the ticket.
# Here, sequence does not matter. The name is the key and the coat is the value.
