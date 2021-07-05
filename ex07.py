# 사용자로부터 숫자(1 - 9)를 하나 입력 받아,
# 구구단을 출력하는 프로그램을 작성해보세요

dan = int(input('출력할 단의 숫자를 입력하세요 (1-9) '))
print(f'{dan} x 1 = {dan * 1} \n' 
      f'{dan} x 2 = {dan * 2} \n' 
      f'{dan} x 3 = {dan * 3} \n'
      f'{dan} x 4 = {dan * 4} \n'
      f'{dan} x 5 = {dan * 5} \n'
      f'{dan} x 6 = {dan * 6} \n'
      f'{dan} x 7 = {dan * 7} \n'
      f'{dan} x 8 = {dan * 8} \n'
      f'{dan} x 9 = {dan * 9}')

# 키보드로 정수를 하나 입력받아 그 값이 양수, 음수, 0인지 구분하는 프로그램을 작성하시오.
# 각각의 경우에 따라 “정수입니다”, “음수입니다”, “0입니다”라고 출력하도록 한다.

num = int(input('정수를 하나 입력하세요'))
result = '정수입니다' if num > 0 else \
         '음수입니다' if num < 0 else '0입니다'
print(result)

# 지금 현재 수지의 통장잔액이 25,000원이다.
# 은행이자가 연 6%라 가정할 때, 몇 년이 지나야
# 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을 작성하세요

balance = 25000
cnt = 0

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')

cnt += 1
ni = balance * 0.06
balance = balance + ni
print(f'{cnt}, {balance:.2f}, {ni:.2f}')











