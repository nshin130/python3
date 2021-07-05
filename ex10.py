# 실전 예제3 전기 요금 계산기

usage = int(input('전기 사용량을 입력하세요'))
rate = 0 # 기본요금
price = 0 # 단가

if usage > 400:
    rate = 7300
    price =280.6
elif usage > 200:
    rate = 1600
    price = 187.9
elif usage <= 200:
    rate = 910
    price = 99.3

fare = rate + (usage * price)
print(f'사용량: {usage:.1f} kwh \n'
      f'기본요금: {rate}원 \n'
      f'단가: {price}원 \n'
      f'전기요금: {fare:,}원')

# usage = int(input('전기 사용량을 입력하세요'))
#
# if usage <= 200:
#     total = 910 + (99.3 * {usage})
#     print(f'기본요금: 910원 \n'
#           '단가: 99.3원 \n'
#           '전기요금 : {total:,}원')
# elif usage <= 400:
#     total = 1600 + (187.9 * usage)
#     print(f'기본요금: 1600원 \n'
#           '단가: 187.9원 \n'
#           '전기요금 : {total:,.1f}원')
# else:
#     total = 7300 + (187.9 * usage)
#     print(f'기본요금: 7300원 \n'
#           '단가: 280.6원 \n'
#           '전기요금 : {total:,.1f}원')