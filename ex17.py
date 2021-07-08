# 회원가입 프로그램
members = {}
flag = True # 프로그램 종류여부 저장하는 변수

menu = '-' * 30
menu += '\n 회원가입 프로그램 \n'
menu += '-' * 30
menu += '\n 1. 성적데이터 입력  \n'
menu += ' 2. 성적데이터 조회  \n'
menu += '-' * 30


while flag:
    print(menu)
    choice = input('작업을 선택하세요:')

    if choice == '1':
        userid = input('아이디는?')
        passwd = input('패스워드는?')
        members[userid] = passwd

    elif choice == '2':
        print('프로그램이 곧 종료됩니다')
        print('가입한 회원들은 다음과 같습니다')

        for u, p in members.items():
            print(f'{u}:{p}')

        flag = False