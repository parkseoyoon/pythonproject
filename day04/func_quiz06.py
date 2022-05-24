#타자게임
#- 데이터는 word = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
#- 문제는 총 5문제가 나옵니다.
#- 나온 문제는 맞힐 때까지 계속됩니다.
#- 문제를 맞히면 다음 문제가 나옵니다.
#- 걸린 시간을 보여줍니다.
#앞의 타자 게임을 활용
#- 1. 문제추가 2. 타자게임 3. 등수리스트 4. 종료하기
#- 문제추가 후 데이터는 파일 저장
#- 문제추가는 단어를 입력받아서 중복되지 않게 추가, 종료 전까지 계속 추가작업 진행
#- 타자게임은 시간을 체크하고, 걸린시간을 사용자명과 함께 저장합니다. (딕셔너리로 저장 : 등수데이터)
#- 등수리스트는 걸린 시간이 적은 순서대로 정렬해서 출력합니다.
#- 종료하기는 등수데이터를 저장하고 진행합니다.
#- 프로그램이 시작될 때 문제와 등수정보를 읽어옵니다.


#word = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf' ]
#rank = {'aaa' : 10.111}

import func_basic1 as fb1

word = fb1.load_save_data('word.json', 'r')
rank = fb1.load_save_data('rank.json', 'r')

while True:
    menu = input('''
1. 문제추가 2. 타자게임 3. 등수리스트 4. 종료하기''')
    
    if menu == '1':
        fb1.quiz_input(word)
        fb1.load_save_data('word.json', 'w', word)
    
    elif menu == '2':
        fb1.typing_game(word, rank)
        
    elif menu == '3':
        fb1.rank_list()

    elif menu == '4':
        print('프로그램을 종료합니다.')
        fb1.load_save_data('rank.json', 'w', rank)
        break
    else :
        print('메뉴선택을 잘못하셨습니다.')