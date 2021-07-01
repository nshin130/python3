import keyword

myName = 'Nara Shin'
myMajor = 'Information System'

print(myName)
print(myMajor)

myName = 100
myName = True
myName = False
myName = 3.141519

intro = 'Hello'
print(intro)
intro = '안녕하세요.'
print(intro)

nickname = 'Mr. Song'
print(nickname)

print(keyword.kwlist)
#print(keyword.softkwlist) # v3.9에서 추가됨

myName = 'Shin'

bigint = 12345555566667777888898989807070060606050505044
print(bigint)

bigfloat = 1.234567891234567890123
print(bigfloat)

a = 123
b = '456'

a = a + 1
#b = b + 1

print(type('안녕하세요.'))
print(type(123))
print(type(True))

print(type(myName))

# 다중 선언
x = 1
y = 1
z = 1

x = y = z = 10

# 자릿수 구분
million = 1000000
million = 1_000_000
num = 1_2_3

# 논리값 확인 : bool
bool(True)
bool(1)
bool(100)
bool(-100)
bool(0)
# python logic: 0일땐 false 양수 음수는 True

# 형변환 함수 ( str() int() float() bool() ) => 빈문자 '' 논리형으로 바꾸면 False, 그 외 나머지 문자 (공백 ' ') True
str(123)
int('456')
float('3.14')

name = input('what is your name? \n')
print(name)

# 이름 국어 영어 수학 성적을 입력받아 출력
name = input('이름을 입력해주세요 \n')
kor = input('국어성적을 입력해주세요 \n')
eng = input('영어성적을 입력해주세요 \n')
mat = input('수학성적을 입력해주세요 \n')

print(name + '/' + kor + '/' + eng + '/' + mat)
print('이름: ' + name)
print('국어: ' + kor)
print('영어: ' + eng)
print('수학: ' + mat)