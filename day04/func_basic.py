#dictionary는 주소값이 넘어오므로 return안해도 됨. 
# but 값이 넘어 올 땐 반드시 return해줘야 함

def menu_input(menu): 
    print('현재메뉴 :', list(menu.keys()))
    name = input('추가할 메뉴명을 입력하세요 >>> ')
    price = 'a'
    while not price.isdecimal():
        price = input('추가할 메뉴의 가격을 입력하세요 >>> ')
    menu[name] = int(price)
    

def menu_update(menu):
    print('현재메뉴 :', list(menu.keys()))
    name = ''
    while not name in menu.keys():
            name = input('수정할 메뉴명을 입력하세요 >>> ')
    price = 'a'
    while not price.isdecimal():
        price = input('수정할 메뉴의 가격을 입력하세요 >>> ')
    menu[name] = int(price)
    

def menu_list(menu):
    print('----- menu -----')
    for item in sorted(menu.items()):
        print(f'{item[0]} : {item[1]:10,}') #10,에서 콤마가 천단위 구분

def menu_delete(menu):
    print('현재메뉴 :', list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('삭제할 메뉴명을 입력하세요 >>> ')
    del menu[name]