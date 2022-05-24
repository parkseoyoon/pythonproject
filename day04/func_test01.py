def test_func(a, b):
    '''
    함수를 작성합니다.  
    '''
    print('test_func 함수 실행', a, b) #'''함수설명'''은 무조건 첫줄에

test_func(1, 'a')

def add1():
    print(1+2)

def add2(a, b):
    print(a+b)
add1()
add2(1, 4)

def add(c, a=1, b=2): #default값을 집어넣으면 add()와 add(1, 4) 둘 다 실행 가능
     print(a+b)     #default값 없는 parameter를 앞쪽에 위치해야함. (c, a=1, b=2) -> 함수 사용할 때 c의 인자값 무조건 넣어야 함
     return c,a,b #return은 안쪽의 값을 바깥으로 전달 & 함수종료를 의미                 

add(1)
add(1, 1, 4)
x = add(1, b=5, a=3)
print(x[1])
x, y, z = add(1, b=4, a=3)
print(x, y, z) 

