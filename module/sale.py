goods = []
flag = True
cnt = len(goods)

while flag:
    menu = input('원하시는 작업을 선택하세요 \n '
          '1.구매 2.종료')

    if menu == '1':
        price = int(input('구매한 상품의 금액을 입력하세요'))
        goods.append(price)

    elif menu == '2':
        flag = False # 반복설정 중지
        rate = 0.7
        sum = 0

        if cnt == 1: rate = 0.95
        elif cnt == 2: rate = 0.9
        elif cnt == 3: rate = 0.8

        for i in range(cnt):
            sum += goods[i]

        tot = sum * rate

        print(f'할인율: {1-rate} \n')
        print(f'총구매금액: {sum} \n')
        print(f'할인적용 구매금액: {tot} \n')

    else:
        print('잘못입력하셨습니다')

def sales(goods):
    rate = 0.3
    sum = 0

    if cnt == 1:
        salesp = price * 0.95
    elif cnt == 2:
        salesp = price * 0.9
    elif cnt == 3:
        salesp = price * 0.8
    else:
        salesp = price * 0.7
    return salesp