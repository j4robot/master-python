def generate_number():
    import random as rd
    chce = [2, 5]
    return f'+233{rd.choice(chce)}{rd.randint(1, 100000000)}'

def remove_duplicates(data):
    temp = []
    for x in range(len(data)):
        if data[x] not in temp:
            temp.append(data[x])
    return temp

data = [
    {'name': 'Emmanuel Achana', 'age': 22, 'level': 5, 'phone': generate_number()},
    {'name': 'Peter Scott', 'age': 18, 'level': 2, 'phone': generate_number()},
    {'name': 'Frank Castle', 'age': 20, 'level': 5, 'phone': generate_number()},
    {'name': 'Stephen Strange', 'age': 27, 'level': 3, 'phone': generate_number()},
    {'name': 'Steve Rogers', 'age': 25, 'level': 4, 'phone': generate_number()},

    {'name': 'Emmanuel Achana', 'age': 22, 'level': 5, 'phone': generate_number()},
    {'name': 'Peter Scott', 'age': 18, 'level': 2, 'phone': generate_number()},
    {'name': 'Frank Castle', 'age': 20, 'level': 5, 'phone': generate_number()},
    {'name': 'Stephen Strange', 'age': 27, 'level': 3, 'phone': generate_number()},
    {'name': 'Steve Rogers', 'age': 25, 'level': 4, 'phone': generate_number()}
]

print(remove_duplicates(data))
print('=====' * 30)
print(data)