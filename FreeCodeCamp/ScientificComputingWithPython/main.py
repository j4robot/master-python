#This is a course on Scientific Computing Using Python 

array = [(x ** 2) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ]
#print(array)

raw = [1, 2, 1, 3, 2, 1, 4, 5]
#print(set(raw))

def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(max_num(5, 1, 3))
    print(__name__)

a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
c = input('Enter an operator: ')

'''
This is a comment for the method.
'''
def calculate(num_a, num_b, op):
    if op == '+':
        return num_a + num_b
    elif op == '-':
        return num_a - num_b
    elif op == '*' or op.lower() == 'x':
        return num_a * num_b
    elif op == '/':
        return num_a / num_b


print(calculate(a, b, c))
