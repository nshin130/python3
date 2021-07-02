# num1 = 10
# num2 = 20
# num3 = num1 + num2 # 정수 + 정수 = 정수
#
# num1 = 30.5
# num2 = 50.5
# num3 = num1 + num2 # 실수 + 실수 = 실수
#
# num1 = 10
# num2 = 30.5
# num3 = num1 + num2 # 정수 + 실수 = 실수
# 작은 데이터 타입이 큰 데이터 타입으로 옯겨가는 것 promotion

# 매출액 구하기
# print('매출을 입력하세요')
# jan = int(input('1월매출을 입력하세요'))
# feb = int(input('2월매출을 입력하세요'))
# mar = int(input('3월매출을 입력하세요'))
# firstQuater = jan + feb + mar
# print('1분기 전체 매출: ' + str(firstQuater))
# print('1분기 전체 매출: {0}원'.format(firstQuater))
#
# num1 = 3.14
# num2 = 0.25
# num3 = num1 + num2
# float(num3)
# num3 = int(num3)

# 1분기 수익 계산
# revenue = int(input('1분기 매출: '))
# cost = int(input('1분기 매입: '))
# profit = revenue - cost
# print('수익: {0}원' .format(profit))

# 방 넓이
# width = int(input('방의 가로 길이: '))
# height = int(input('방의 세로 길이: '))
# area = width * height
# print('방 넓이는 {0}㎠'.format(area))
#
# str1 = 'hello world '
# str1 * 3
# 2 * str1 * 3
# str1 * -2
# str1 * 0.1 (not working)
# 문자열의 나눗셈 (not working)

# BMI
# ~18.5 : 저체중
# ~23 : 정상
# ~25: 과체중
# ~30 : 비만
# 30~ : 고도비만
# height = int(input('키를 입력하세요'))
# weight = int(input('몸무게를 입력하세요(kg)'))
# height = height / 100
# bmi = weight / (height*height)
# print('BMI지수는 {0:.2f}%입니다'.format(bmi))
# print(f'BMI지수는 {bmi:.2f}%입니다') # f-string: py3.6 부터 지원

# print 출력 속도 : f-string -> % -> .format

# 동전 갯수 알아보기
# coin = int(input('손 안에 동전 수를 입력하세요 '))
# evenorodd = coin % 2
# print(evenorodd)
# print(f'동전의 홀짝여부 (0:짝/1:홀) {evenorodd}')
#
# 10/3
# 10//3

# 빵 나눠주기
# bread = int(input('빵의 갯수는?'))
# divid = int(input('나눠줄 빵의 갯수는?'))
# students = bread // divid
# leftover = bread % students
# print(f'{bread}개의 빵은 {divid}씩 {students}명의 학생에게 나줘줄수 있고 남는 빵의 갯수는 {leftover}')

2**3
2**7
2**8

# 전염병 예상 감염자 수
expected = 2**30
print(f'30일 뒤 예상 감염자는 {expected}명이다')

# 복리계산
principal = 5000000
times = 5
interest = 0.05
compound = 1

money = 5_000_000
duration = 5
interest = 5.0

takes = money + (money * 0.05)
takes += money * 0.05
takes += money * 0.05
takes += money * 0.05
#
# height = int(input('키를 입력하세요'))
# print(f'탑승 가능여부 {height > 120} (True: 탑승가능)')

'a' == 'b'
'a' > 'b'
# ASCII code 로 변환 후 비교

# height = int(input('키를 입력하세요'))
# isride = 120 <= height < 170
# #isride = 120 <= height and height < 170
# print(f'탑승 가능여부: {isride} (True: 탑승가능 False: 탑승불가능)')

(10 > -10) and (3.14 > 0) or (-1 == 0)

# short circuit evaluation
num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15) # False

num1 = 10
num2 = 20
(num1 < 15) or (num2 < 15) # True

# (num1 < 5) and xyz

# 삼항 연산자
# 참일때 값 if 조건식 else 거짓일때 값

num = 11
'짝수' if (num % 2 == 0) else '홀수'

# 적자 흑자 알아보기
income = int(input('수입을 입력하세요'))
expenses = int(input('비용을 입력하세요'))
result = '흑자' if (income > expenses) else '적자'
print(result)

# 윤년여부 알아보기 : 4로 나눠떨어지고 100 으로 나눠 떨어지지 않음 or 400 으로 나눠 떨어짐
year = int(input('윤년여부를 알아보고 싶은 년도를 입력하세요'))
leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
result = '윤년입니다' if (leap) else '평년입니다'
print(result)

# operator module -> 대량의 데이터 처리시 속도 향상이 존재함
import operator as op
op.add(10,20)
op.sub(10,20)
op.mul(10,20)
op.floordiv(10,3) # 정수 몫: //
op.truediv(10,3) # 실수 몫: /
op.mod(10,3) # 나머지
op.pow(2,30) # power (제곱승)

op.eq(10,20)
op.ne(10,20)
op.gt(10,20)
op.lt(10,20)
op.ge(10,20)
op.le(10,20)

y = op.eq(10,20)
x = op.ne(10,20)
op.and_(x, y)
op.or_(x, y)

# 긴급 재난 지원금 대상자 판별
money = int(input('월소득: '))
con2 = int(input('다른 지원금을 받고 있다면 1번 받고있지 않다면 2번을 누르세요'))
import operator as op
con1 = op.le(money,4_000_000)
con22 = op.eq(con2, 2)
result = '수급대상자' if (con1 and con22) else '수급 대상자가 아닙니다'

isTarget = op.and_(op.le(money,4_000_000), op.eq(con2, 2))
result = '수급대상자' if (isTarget) else '수급미대사장'

print(result)

