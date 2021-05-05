#Create a dictionary
dictionary = {'name': 'Achana', 'age': 25, 'sex': 'Male', 'skills': ['programming', 'drawing', 'singing', 'gaming']}

#Dictionary in array format. 
print(dictionary.items())

# Dictionary methods to get the keys and values respectively.
print(dictionary.keys())
print(dictionary.values())

#Get the keys as list.
print(list(dictionary))

#Get the keys as list which is also sorted.
print(sorted(dictionary))

#Add new key and value
dictionary['phone'] = '0547022937'
print(dictionary)

#Delete key, value.
del dictionary['skills']
print(dictionary)

#Check if a particular key is in the dictionary
is_skill_available = 'skills' in sorted(dictionary)
print(is_skill_available)

#The dict() constructor build dictionaries directly from sequences of key : value
dictionary = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print(dictionary)

#Dict comprehensions can be used to create dictionaries from arbitrary key and value expressions
dictionary = {x: x**2 for x in (2, 4, 6)}
print(dictionary)

#When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
dictionary = dict(sape=4139, guido=4127, jack=4098)
print(dictionary)