# 369
# for i in range(1, 99+1):
#     clap = ''
#     if i % 3 == 0 or i % 6 == 0 or i % 9 == 0:
#         clap = '짝!'
#     print(f'{i} {clap}')

for i in range(1, 100):
    clap = ''
    if i < 10: # 숫자가 한자리라면
        if i % 3 == 0:
            clap = '짝!'
    else: # 숫자가 두자리라면
        num1 = i // 10 # 첫째 숫자 추출
        num2 = i % 10 # 나머지 숫자 추출

        if num1 % 3 == 0: # 첫째 숫자가 3의 배수라면
            clap += '짝!'

        if num2 % 3 == 0 and num2 != 0: # 둘째 숫자가 3의 배수이고 0이 아니라면
            clap += '짝!'

    print(f'{i} {clap}', end=' ')
print()


