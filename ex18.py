# 다국어 인삿말

def sayHello(nation):
    if nation == '1':
        print('안녕하세요')

    elif nation == '2':
        print('Hello')

    elif nation == '3':
        print('こんにちは')

    elif nation == '4':
        print('你好')

    else:
        print('잘못 입력하셨습니다')


nation = input('당신의 국적은? \n 1. 한국 2. USA 3. Japan 4.China \n')

sayHello(nation)