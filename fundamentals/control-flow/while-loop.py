def fibonacci(num):
    a, b = 0, 1
    temp = []
    while a < num:
        temp.append(a)
        a, b = b, a+b
    return temp

print(fibonacci(150))