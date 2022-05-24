def add(*args): #parameter에 *하면 여러개의 인자를 넣을 수 있음
    total = 0
    for i in args:
        total += i
    return total

total = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(total) 

def mul(a, b, c, d):
    print(a*b*c*d)

mul(*[1, 2, 3, 4]) #list(tuple) 앞에 *를 붙이면 unpacking -> 리스트의 포장을 푼다. 숫자를 각각 인식 
