def generate_number():
    import random as rd
    chce = [2, 5]
    return f'+233{rd.choice(chce)}{rd.randint(1, 100000000)}'

def remove_duplicates(data):
    res = [] 
    for i in range(len(data)): 
        if data[i] not in res:
            res.append(data[i]) 
    return res

# def remove_duplicates(dict_array):
#     return [i for n, i in enumerate(dict_array) if i not in dict_array[n + 1:]]

data = [
    {'name': 'Emmanuel Achana', 'age': 22, 'level': 5, 'phone': '+233566831631'}, 
    {'name': 'Peter Scott', 'age': 18, 'level': 2, 'phone': '+233536496890'}, 
    {'name': 'Frank Castle', 'age': 20, 'level': 5, 'phone': '+233253006512'}, 
    {'name': 'Stephen Strange', 'age': 27, 'level': 3, 'phone': '+233546939676'}, 
    {'name': 'Steve Rogers', 'age': 25, 'level': 4, 'phone': '+233528052634'}, 
    {'name': 'Emmanuel Achana', 'age': 22, 'level': 5, 'phone': '+233566831631'}, 
    {'name': 'Peter Scott', 'age': 18, 'level': 2, 'phone': '+233536496890'}, 
    {'name': 'Frank Castle', 'age': 20, 'level': 5, 'phone': '+233253006512'}, 
    {'name': 'Stephen Strange', 'age': 27, 'level': 3, 'phone': '+233546939676'}, 
    {'name': 'Steve Rogers', 'age': 25, 'level': 4, 'phone': '+233528052634'}
]

print('=====' * 20)
print(remove_duplicates(data))
print('=====' * 20)

newList = [i for i in range(1,3)]
print(newList)