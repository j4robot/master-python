

def fibonacci(num) -> list:
    '''This is a function for running a fibonacci sequence.
    
       It takes an int as the argument to show how many times the process is run. 
    '''
    a, b = 0, 1
    temp = []
    while a < num:
        temp.append(a)
        a, b = b, a + b
    return temp

dvdr = '-----' * 10

# print(fibonacci(12))
# print(dvdr)

even = list(range(2, 11, 2))
# print(even)
# print(dvdr)

def some(name, age, color):
    print(f'The name is {name}')
    print(f'I am {age} years old')
    print(f'My favorite color is {color}')

args = {'name': 'Emmanuel Achana', 'age': 25, 'color': 'army green'}

# some(**args)

