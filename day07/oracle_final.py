import cx_Oracle

conn = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("create table fruit(product varchar2(20), stock number(3), price number(10), receive number(8), sweet number(1))")
          
#수정
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