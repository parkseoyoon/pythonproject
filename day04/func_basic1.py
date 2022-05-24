import random, time, json, os

def load_save_data(file, mode, data=None): #data=None은 들어올 때도 있고 나갈 때도 있을 때 사용, 오류방지
    path = os.path.dirname(__file__) + '/' + file
    print(os.path.dirname(__file__))
    with open(path, mode) as f:
        if mode == 'r':
            data = json.load(f)
            return data
        elif mode == 'w':
            json.dump(data, f)
        

def quiz_input(word):
    while True:
        quiz = input('추가할 단어를 입력(종료:0) >>> ')
        while quiz in word :
            quiz = input('중복된 단어입니다. 다시 입력(종료:0) >>> ')
        if quiz == '0':
            break
        word.append(quiz)
        print(word)
    # load_save_data('word.json'.'w', word)

def typing_game(word, rank):
    n = 1
    quiz = random.choice(word)
    input('시작!(enter)')
    start = time.time()
    while n <= 5:
        print(f'{n}번')
        print(quiz)
        x = input()
        if quiz == x:
            print('통과!')
            n += 1
            quiz = random.choice(word)
        else:
            print('오타! 다시 도전!')
    print('5문제 다 맞혔습니다.')
    end = time.time()
    print(f'걸린시간:{end-start:.0f}초')
    name = input('사용자명을 입력하세요 >>> ')
    while name in rank:
        name = input('사용자명이 중복됩니다.다른 이름을 입력하세요 >>> ')
    rank[name] = end-start
    print(rank)


def rank_list():
    print('<등수리스트>')
    ranklist = sorted(rank.items(), key = lambda x:x[1])
    for index, item in enumerate(ranklist):
        print(f'{index+1}등 {item[0]} {item[1]:.2f}초')
