# 파일 다루기


# 입력한 성적데이터를 파일에 저장
fname = '/Users/nara/01JAVAb/SungJuk.data'

name = input('이름은?')
kor = int(input('국어는?'))
eng = int(input('영어는?'))
mat = int(input('수학은?'))

f = open(fname, 'w')  # 지정한 파일을 쓰기모드로 open
# data = 'hello world'
data = f'{name},{kor},{eng},{mat}'  # 파일에 기록할 내용을 문자열로 작성
f.write(data)
f.close()

# 기록한 성적데이터를 파일로부터 읽어오기
f = open(fname, 'r')  # r => read
data = f.read()
print(data)
f.close()


# 일정 관리 메모를 입력하여 텍스트 파일에 저장하기
def saveMemo(memo):
    fname = '/Users/nara/01JAVAb/myMemo.txt'
    f = open(fname, 'a')
    f.write(memo + "\n")
    f.close()


def memoMain():
    memo = input('메모를 입력하세요')
    saveMemo(memo)


memoMain()

# py3 방식으로 파일 다루기
# 기존 파일 입출력 코드에서 불편한 점은
# 파일작업후에는 반드시 close 해야 한다는 것
# with 문을 사용하면 명시적으로 close를 사용하지 않아도 됨
with open(fname, 'w') as f:
    f.write('hi hello bye')

# 파일에서 데이터 읽어오기
fname = '/Users/nara/01JAVAb/EMPLOYEES.csv'
with open(fname) as f:
    data = f.read()  # 모든 데이터를 한번에 다 읽어옴
    print(data)

with open(fname) as f:
    data = f.readline()  # 데이터를 한줄 읽어옴
    print(data)

with open(fname) as f:
    data = f.readlines()  # 모든 데이터를 라인단위로 읽어옴
    print(data)  # 읽어온 결과는 list형식

# EMPLOYEES.csv 에서 사번, 이름, 입사일, 급여를 출력하세요
with open(fname) as f:
    f.readline()  # 첫줄은 읽기만 함 (header때문)
    while True:
        line = f.readline()
        if not line: break  # 읽을 데이터가 없는 경우 작업중단
        data = line.split(',')  # 문자열을 , 로 분리해서 리스트로 저장

        empno = data[0]
        name = data[1]
        hdate = data[5]
        sal = int(data[7])

        emp = f'{empno} {name} {hdate} {sal:,}'
        print(emp)

# 타이타닉 데이터셋을 이용해서
# 승객이름, 성별, 나이, 승선위치, 사망여부등을 추출해서 출력하세요
# name, sex, age. embarked, survived
# 단 survived가 0이면 '사망' 1이면 '생존'이라고 출력함
# emarked가 s이면 'southampthon' c이면 'cherbourg', Q라면 'queenstown'이라 출력

fpath = '/Users/nara/downloads/titanic3b.csv'

with open(fpath) as f:
    f.readline()
    while True:
        line = f.readline()
        if not line: break

        data = line.split(',')

        # name = data[2]
        sex = data[2]
        age = data[3]
        pos = data[9]
        live = data[1]

        if pos == 'S':
            pos = 'Southampton'
        elif pos == 'Q':
            pos = 'Queenstown'
        elif pos == 'C':
            pos = 'Cherbourg'

        if live == '0':
            live = '사망'
        elif live == '1':
            live = '생존'

        if age == '':
            age = '0'

        result = f'{sex} {age} {pos} {live}'
        print(result)
