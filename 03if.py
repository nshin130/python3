# if문
# num = int(input('숫자를 하나 입력하세요'))
# if (num > 10):
#     print('숫자가 10보다 큽니다')

# 속도 위반 경고 프로그램
# speed = int(input('현재 속도를 입력하세요'))
# if (speed > 50):
#     print('속도 위반!!!')
#     print('속도를 줄이세요')

# if speed > 50: print('속도 위반!!!')

# 합격 불합격 출력: if ~ else
# score = int(input('점수를 입력해 주세요 '))
# if score >= 80:
#     print('합격입니다')
# else:
#     print('불합격입니다')
#
# # pass: 실행문이 아직 정해지지 않은 경우 pass 키워드로 대체 작성 가능 (오류 x)
# # score = int(input('점수를 입력해 주세요'))
# # if score >= 80:
# #     pass
# # else:
# #     pass
#
# # 온도 감지 프로그램
# temp = int(input('기계 온도를 입력해주세요 '))
# if temp > 40:
#     print('팬(Fan) 가동')
# else:
#     print('팬(Fan) 중지')
#
# # 입력받은 정수를 3으로 나눠 소수점 첫째자리에서 반올림하는 프로그램
# num = int(input('양수를 입력하세요'))
# result = num / 3
#
# if (result - int(result) >= 0.5):
#     result = int(result) + 1
# else:
#     result = int(result)
# print(f'결과: {result}')
#
# # 조건문 프로그램
# mileage = 1200
# if mileage >= 1000:
#     print('마일리지 사용가능')
# else:
#     print('마일리지 사용불가')
#
# # 성적 처리
# score = int(input('점수를 입력하세요'))
#
# if 60 <= score < 70:
#     print('D-양')
# elif 70 <= score < 80:
#     print('C-미')
# elif 80 <= score < 90:
#     print('B-우')
# elif 90 <= score <= 100:
#     print('A-수')
# else:
#     print('F-가')
#
# # 자동 주문 시스템
# intro = '안녕하세요, 만나서 반갑습니다 \n' \
#       '어디서 오셨나요? 번호를 선택하세요 \n' \
#       '1.대한민국 2.USA 3.China'
# nation = input(intro)
#
# intro = 'Would you like to order?'
# if (nation == '1'):
#     intro = '주문하시겠어요?'
# elif (nation == '2'):
#     intro = 'Would you like to order?'
# elif (nation == '3'):
#     intro = '대충 중ㅇ국어로 주문하겠냐는글'
# else:
#     intro = 'Would you like to order?'
#
# print(intro)
#
# # 국가재난지원금 수령액 조회
# count = int(input('인원수를 입력하세요 '))
#
# if count == 1:
#     money = 400_000
# elif count == 2:
#     money = 600_000
# elif count == 3:
#     money = 800_000
# else:
#     money = 1_000_000
# print(f'{money:,}원 지원')
#
# # BMI 지수를 계산하고 다양한 결과를 출력
#
# height = int(input('키를 입력하세요'))
# weight = int(input('몸무게를 입력하세요'))
# height = height * 0.01
#
# bmi = weight / (height * height)
# if bmi > 30:
#     print('고도비만')
# elif bmi > 25: print('비만')
# elif bmi > 23: print('과체중')
# elif bmi > 18.5: print('정상체중')
# else: print('저체중')
# print(f'{bmi:.1f}')

# 버스 전용차로 단속 프로그램
day = input('1.월~금 2.토요일 3.공휴일 \n'
            '요일을 선택하세요.')
if day == '1':
    car = input('버스 전용차로 단속 중입니다 \n'
          '1.버스 2.승용차 \n'
          '차종을 선택하세요.')
    if car == '1': print('버스입니다.')
    else: print('버스 전용차로 위반!')
else:
    print('토요일 및 공휴일은 단속하지 않습니다')

# 마스크 구매 요일 출력 프로그램
age = input('만 나이를 입력하세요')
if (age < '65'):
    endByear = int(input('출생 연도 끝자리를 입력하세요'))
    if endByear == 1 and 6:
        print('월요일 구매 가능합니다')
    elif endByear == 2 and 7:
        print('화요일 구매 가능합니다')
    elif endByear == 3 and 8:
        print('수요일 구매 가능합니다')
    elif endByear == 4 and 9:
        print('목요일 구매 가능합니다')
    else:
        print('금요일 구매 가능합니다')
else:
    print('언제든지 구매가 가능합니다.')

