# 과일가게 재고 프로그램 구축

# 프로그램 최초 실행시 테이블 생성(cursor.execute("create~~"))
# 테이블명 fruit
# 열이름 product(가변형 문자열 20자리), stock(정수형 숫자 3자리), price(정수형 숫자 10자리), receive(정수형 숫자 8자리), sweet(정수형 숫자 1자리)

# 1. 기능
# 과일 입력(I), 과일 판매(S), 재고 리스트(L), 품절품목확인(C), 삭제(D), 종료(Q)
# 괄호 안 영문자를 입력하면 각 기능이 구현되게 만든다

# 2. 입력(I) 
# 상품명(product), 수량(stock), 가격(price), 입고일자(receive), 당도(sweet)를 입력받아 테이블에 행을 추가한다.
# 입고일자(receive):8자리(YYYYMMDD)로 입력해야함

# 3. 판매(S)
# 현재 테이블에 있는 상품리스트를 모두 보여준다.
# 과일명(name)과 판매된 수량(sold)을 입력받아 해당되는 과일의 stock값을 stock-sold값으로 변경(update)한다. 

# 4. 재고리스트(L)
# product(오름차순), stock(오름차순), receive(오름차순), sweet(내림차순) 에 따라 정렬 가능하게 한다.

# 5. 품절품목확인(C)
# 현재 재고(stock)가 0인 과일명을 테이블에서 가져와 보여준다.

# 6. 삭제(D)
# 현재 테이블에 있는 상품리스트를 보여준다.
# 삭제하고 싶은 과일명(name)을 입력받아 테이블에서 해당되는 행을 삭제한다.

# 7. 종료(Q)
# 프로그램을 종료하면서 oracle과 연결을 닫는다.
# (cursor.close() 와 conn.close())

import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("select count(*) from all_tables where table_name = 'fruit'")
if cursor == 0:
    cursor.execute("create table fruit(product varchar2(20), stock number(3), price number(10), receive number(8), sweet number(1))")
          
while True:
    choice=input('''
다음 중에서 하실 일을 골라주세요 :
I - 입력 \t S - 판매 \t L- 재고 리스트 \t C-품절품목확인 \t D-삭제 \t Q-종료
>>> ''').upper()

    if choice == 'I':
        sql = "insert into fruit values(:1,:2,:3,:4,:5)"
        product = input('과일명 >>> ')
        stock = input('수량 >>> ')
        price = input('가격 >>> ')
        receive = input('입고일자(8자리 YYYYMMDD) >>> ')
        sweet = input('당도 >>> ')
        data = (product, int(stock), int(price), int(receive), int(sweet))
        cursor.execute(sql, data)
        conn.commit()

       
    elif choice == 'S':
        cursor.execute("select * from fruit")
        for item in cursor:
            print(f'{item[0]}, 수량 : {item[1]}, 가격 : {item[2]}, 입고일자 : {item[3]}, 당도 : {item[4]}')
        sql = "update fruit set stock = stock - :1 where product = :2"
        name = input('판매된 과일명 >>> ')
        sold = input('판매된 수량 >>> ')
        data = (int(sold), name)
        cursor.execute(sql, data)
        conn.commit()

                                   
    elif choice == 'L':
        while True:
            choice = input('''
다음 중에서 분류하실 종목을 골라주세요 :
1. product \t 2.stock \t 3.receive \t 4.sweet
>>> ''')
            if choice == '1':
                cursor.execute("select * from fruit order by product")
                for item in cursor:
                    print(f'{item[0]}, 수량 : {item[1]}, 가격 : {item[2]}, 입고일자 : {item[3]}, 당도 : {item[4]}')
             
            
            elif choice == '2':
                cursor.execute("select * from fruit order by stock")
                for item in cursor:
                    print(f'{item[0]}, 수량 : {item[1]}, 가격 : {item[2]}, 입고일자 : {item[3]}, 당도 : {item[4]}')
            

            elif choice == '3':
                cursor.execute("select * from fruit order by receive")
                for item in cursor:
                    print(f'{item[0]}, 수량 : {item[1]}, 가격 : {item[2]}, 입고일자 : {item[3]}, 당도 : {item[4]}')
            

            elif choice == '4':
                cursor.execute("select * from fruit order by sweet desc")
                for item in cursor:
                    print(f'{item[0]}, 수량 : {item[1]}, 가격 : {item[2]}, 입고일자 : {item[3]}, 당도 : {item[4]}')
            
            else:
                print('다시 선택해주세요')    
                break
    
    elif choice == 'C':
        cursor.execute("select product from fruit where stock = 0")
        for i in cursor:
            print(f'품절된 과일:{i}')

    elif choice == 'D':
        cursor.execute("select * from fruit")
        for item in cursor:
            print(f'{item[0]}, 수량 : {item[1]}, 가격 : {item[2]}, 입고일자 : {item[3]}, 당도 : {item[4]}')
        sql = "delete from fruit where product = :1"
        name = input('삭제할 과일명 >>> ')
        cursor.execute(sql, (name,)) #tuple형태는 하나일 때 반점과 함께 써야 함
        conn.commit()
        

    elif choice == 'Q':
        print('프로그램을 종료합니다')
        cursor.close()
        conn.close()
        break

    else:
        print('다시 입력해주세요')