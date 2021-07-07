# list (FIFO) 순차적으로 나열하고자 할때
# 참조자료형(데이터의 메모리 주소가 담김)
# 리스트 안에 각각의 데이터를 아이템 또는 요소라고 함

attendList = ['순철', '병헌', '민우', '찬호', '민태']
print(attendList)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

complex = [1, 2.0, 3.1415, 40, '5', "6"]
print(complex)

for data in numbers: # iterable
    print(data)

for data in complex: # iterable
    print(data)

len(numbers)
len(complex)

msg = 'Hello, World'
len(msg)

msg = input('메시지를 입력하세요')
print(f'문자열의 길이: {len(msg)}')

print(len(['Hello, Python!!']))
print(len('Hello, Python!!'))

# list의 모든 항목 조회
print(complex[0])
print(complex[1])
print(complex[2])
print(complex[3])
print(complex[4])
print(complex[5])

for i in range(len(complex)):
    print(complex[i])

# 향상된 for문을 이용해 리스트 출력하기
for item in complex:
    print(item)

# enumerate()함수를 이용해 리스트 조회: 앞에 인덱스 뒤에 아이템
for idx, item in enumerate(complex):
    print(f'{idx}, {item}')

print(complex.index(3.1415))

sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
print(f'마지막 인덱스 값은 {len(sports)-1} 입니다')

languages = ['c/c++', 'c#', 'python', 'java']
print(languages.index('python'))

hobbies = ['reading', 'hiking', 'cooking']
hobbies.append('volleyball')
print(hobbies)

numbs = [1, 2, 3, 4, 5, 7, 8, 9]
numbs.insert(5, 6)
numbs.append(10)
print(numbs)

weather = ['The', 'weather', 'very']
weather.insert(2, 'is')
print(weather)
weather.insert(4, 'cold')

# 성적 처리 프로그램 3명 총점 평균 학점
names = []
kors = []
engs = []
mats = []

for i in range(3):
    name = input('이름은?')
    names.append(name)
    kor = int(input('국어는?'))
    kors.append(kor)
    eng = int(input('영어는?'))
    engs.append(eng)
    mat = int(input('수학은?'))
    mats.append(mat)

tots = []
avgs = []
grds = []
for i in range(3):
    tots.append(kors[i] + engs[i] + mats[i])
    avgs.append(tots[i] / 3)
    grds.append('가')
    if avgs[i] >= 90:grds[i] = '수'
    elif avgs[i] >= 80:grds[i] = '우'
    elif avgs[i] >= 70:grds[i] = '미'
    elif avgs[i] >= 60:grds[i] = '양'

for i in range(3):
    print(f'{names[i]}, {kors[i]}, {engs[i]}, {mats[i]}\n'
          f'{tots[i]}, {avgs[i]:.1f}, {grds[i]}\n')

# 리스트 수정
# 리스트[인덱스] = 수정할 값
hobbies[1] = 'traveling'
hobbies

# 리스트 삭제
# pop() => 맨뒤의 항목을 제거
# 괄호안에 인덱스 넘버를 넣으면 그 위치의 아이템이 삭제됨
hobbies
delete = hobbies.pop()
delete

sports
sports.pop(2)

# remove() => 요소값으로 제거
languages
languages.remove('c/c++')

fuits = ['apple', 'mango', 'carrot', 'watermelon', 'grape', 'korean melon', 'tomato']
fuits.pop(2)
fuits.remove('tomato')
fuits


scores = [55, 65, 40, 70, 65, 70]

cnt = len(scores)
sum = 0
fail = 0
result = '아쉽지만 불합격입니다'

for i in range(cnt):
    if scores[i] < 40: fail += 1
    sum += scores[i]
avg = sum / cnt
if fail == 0 and avg >= 60:
    result = '합격입니다'

print(f'평균점수 : {avg:.2f}')
print(result)

# 정렬하기
numbers = [5, 1, 3, 4, 2, 6]
numbers.sort()
numbers

numbers.sort(reverse=True)
numbers

test = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
test.sort(reverse=True)
test

# 문자 정렬 (한글)
names = ['김길동', '빅길동', '이길동', '정길동', '홍길동']
names.sort(reverse=True)
names

# 문자 정렬 (영어)
units = ['scv', 'marine', 'firebat', 'ghost', 'dropship', 'battlecruiser', 'valkryrie']
units.sort(reverse=True)
units

# list slicing
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alphabet.sort(reverse=True)
alphabet

alphabet[2:6]
alphabet[0:5]
alphabet[:5]
alphabet[3:8]
alphabet[5:10]
alphabet[5:]
alphabet[3:9]
alphabet[-4:]

# a b c d 추출
alphabet[:4]
alphabet[0:4]
alphabet[0:-6]

# 슬라이싱 고급기능
alphabet[::-1]
alphabet[1::-1]
alphabet[3::-1]
alphabet[:-3:-1]

# d c b a 추출
alphabet[3::-1]
alphabet[-7::-1]
alphabet[-7:-11:-1]

# g h e d 추출



