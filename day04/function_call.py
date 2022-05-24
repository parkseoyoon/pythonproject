def mul(a, b):
    c = a * b
    return c
 
def add(x, y):
    c = x + y
    x+=10
    y+=10
    print('x', x, 'y', y)
    print(c)
    d = mul(x, y)
    print(d)
 
x = 10
y = 20
add(x, y)
print('x', x, 'y', y)