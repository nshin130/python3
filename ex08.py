# 실전 예제1 차량 2부제 프로그램
#today = int(input('오늘 날짜를 입력하세요'))
from datetime import datetime as dt
day = dt.now().day
day = dt.today().day

plate = int(input('차량번호 4자리를 입력하세요'))

if ( day % 2 == 0):
    if plate % 2 == 0:
        print('귀하의 차량은 입차 가능합니다')
    else:
        print('귀하의 차량은 입차 불가능합니다')
else:
    if plate % 2 != 0:
        print('귀하의 차량은 입차 가능합니다')
    else:
        print('귀하의 차량은 입차 불가능합니다')

# 쌤코드
day = input('todays date?')
car = input('plate number?')

evenorOdd = 'even'
if int(day) % 2 != 0: evenorOdd = 'odd'
print(f'오늘 입차: 번호가 {evenorOdd}인 차량')

passorNot = '입차불가능'
if int(car) % 2 == 0 and evenorOdd == 'even':
    passorNot = '입차 가능'
print(f'귀하의 차량은 {passorNot} 합니다')
