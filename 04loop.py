# 반복문
# 1 ~ 10까지 정수 출력
for i in range(1, 10+1):
    print(i)

# 2 ~ 10 짝수
for i in range(2, 10+1, 2):
    print(i, end=' ')
    #print(i)

# 2 ~ 8 짝수
for i in range(2, 8+1, 2):
    print(i)

# 사용자가 입력한 횟수만큼 문자열 출력
num = int(input('메일 발송 횟수를 입력해주세요'))
msg = '메일 발송!'
for i in range(1, num+1):
    print(msg)

# 1 ~ 10 사이 정수 출력 , 정수가 3의배수이면 3의 배수 출력하기
for i in range(1, 1+10):
    if (i % 3 == 0): print('3의 배수!')
    else: print(f'num {i}')

# 구구단 출력
dan = int(input('단을 입력하세요'))
for i in range(1, 9+1):
    print(f'{dan} x {i} = {dan * i}')

# 1-10 정수 합
sum = 0
for i in range(1, 10+1, 1):
    sum += i
print(sum)

for i in range(1, 100+1):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

min = 100
print('3과 7의 공배수', end=' ')
for i in range(100, 1, -1):
    if i % 3 == 0 and i % 7 == 0:
        if min >= i: min = i
        print(i, end=', ')
print(f'최소공배수 {min}')

for i in range(-10, 1, 1):
    print(i, end=', ')

# 1 ~ 10 까지 출력
for i in range(10):
    print(i+1, end=' ')

# 반복문에 range대신 문자열 사용
for ch in 'Hello':
    print(ch, end=',')

# 50 보다 작은 7의 배수
for i in range(7, 50+1 ,1):
    if i % 7 == 0:
        print(i, end=' ')

for i in range(50):
    if i % 7 == 0:
        print(i, end=' ')
print()

# while : 결과가 참일때 반복
# 1 ~ 10 출력
num = 1
while num < 10+1:
    print(num)
    num += 1

# 1 ~ 30 홀짝 구분해 출력하기
num = 1
while num <= 30:
    if num % 2 == 0: print(f'짝수:{num}')
    else: print(f'홀수:{num}')
    num += 1

# 구구단 3단 출력
num = 1
dan = 3
while num < 9+1:
    print(f'{dan} x {num} = {dan * num}')
    num += 1

# 0 ~ 100 정수 3과 8의 공배수와 최소공배수 출력하기
num = 0
min = 100
while num < 100+1:
    if num % 3 == 0 and num % 8 == 0 and num > 0:
        print(f'공배수: {num}')
        if min > num: min = num # 첫번째로 나오는 숫자만 저장하기 위함(초기화하는 숫자는 상관무)
    num += 1
print(f'최소공배수: {min}')

# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1:진행 2:종료'))
    if code == 1:
        print('게임 진행')
    else:
        flag = False
        print('게임 종료')

# 1 ~ 50 정수중 3의 배수를 더하기
sum = 0
for i in range(1, 50+1):
    if i % 3 == 0:
        sum += i
print(sum)

sum = 0
for i in range(1, 50+1):
    if i % 3 != 0: continue
    sum += i
print(sum)

# 1 ~ 100 까지 모든 정수 더하기
# 단 정수의 합이 500이 넘었을때의 정수는 무엇인가
sum = 0
for i in range(1, 100+1):
    sum += i
    if sum >= 500:
        print(i)
        break
print(sum, i)

# 1 ~ 10 까지 정수의 총합을 구하고
# 반복이 끝나는 경우 완료 메시지 출력
sum = 0
for i in range(1, 10+1):
    sum += i
else:
    print(f'총합 계산 끝: {sum}')

# 삼각형 넓이 구하기
width = 2
height = 3
area = 0
while area <= 150:
    area = width * height * 0.5
    print(area, width, height)
    width += 2
    height += 3

# 1-100 까지 정수 출력 5와 7의 정수제외하고 출력
for i in range(1,100+1):
    if i % 5 == 0 or i % 7 == 0:
        continue
    else:
        print(i, end=' ')
print()


# 구구단 출력
for i in range(1, 19+1):
    for j in range(1, 19+1):
        print(f'{j:2d} x {i:2d} = {i * j:2d} \t', end=' ')
    print()
print()

# 별트리 출력
print('     *')
print('    ***')
print('   *****')
print('  *******')
print(' *********')


