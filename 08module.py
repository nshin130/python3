# 패키지 package
# 함수, 클래스들을 용도별로 분리해서
# 작성하는 것을 모듈이라 했음

# 그런데, 이러한 모듈들이 모여 뒤죽박죽 섞여 있으면
# 이해도, 활용도가 떨어질수 있음

# 따라서, 모듈들 역시 성격에 맞게 분류해서 관리해야 할
# 필요성이 대두 - 패키지를 이용해서 모듈들을 관리

# 파이썬에서는 패키지를 만들려면
# 디렉토리 생성 -> __init__.py 파일 생성하면 됨 (py2)
# python3 이상 __init__.py 를 만들지 않아도
# 패키지로 인식
# => python2와의 호환을 위해 생성할 것을 권장

# 모듈 불러오기
# import packageName.moduleFileName

import module.calculator

module.calculator.add(3, 5)
module.calculator.subs(3, 5)
module.calculator.mult(3, 5)
module.calculator.divd(3, 6)

# 단위 변환 프로그램
import module.ConvertUnit

data = int(input('변환할 길이(mm)를 입력하세요'))

result = module.ConvertUnit.convertLength(data)
module.ConvertUnit.printUnits(result)

# 시험 합격여부
import module.exam

kor = int(input('국어는?'))
eng = int(input('영어는?'))
mat = int(input('수학은?'))
tot, avg, ispass = module.exam.examResult(kor, eng, mat)

print(f'총점:{tot} \n 평균:{avg:.2f}\n 합격여부:{ispass}')

# 모듈명 줄여쓰기 : as
import module.calculator as mcc
import module.ConvertUnit as mcu
import module.exam as me

mcc.add(3,5)
mcc.mult(3,5)
mcu.convertLength(20)
me.examResult(54,67,97)

# 모듈중에서 특정 함수만 사용하고 싶을때는
# 'from 모듈명 import 함수명' 형식을 사용

from module.calculator import add
from module.calculator import subs # 가독성을 위해 추천

from module.calculator import add, divd

# 수학모듈
import math as m

print(m.ceil(10.5))
print(m.floor(10.9))

import random as r
print(r.random())
print(r.randint(1,45)) # 1 ~ 45
print(r.randrange(1,45)) # 1 ~ 44
print(r.sample(range(1,10),3)) # 표본추출
print(r.choice(range(1,10)))

# 점심메뉴 추천 프로그램
lunches = ['양꼬치', '햄버거', '피자', '옥수수', '불고기']

idx = r.sample(range(10),1)[0]
idx = r.randint(0,9)
idx = r.randrange(0,10)
idx = r.choice(range(10))
print(f'오늘의 점심메뉴는{lunches[idx]}')

print(r.choice(lunches))

import time as t
print(t.time())
print(t.localtime()) # 요일(wday)은 월요일 기준으로 0~7

fmt = '%Y-%m-%d %H:%M:%S'
print(t.strftime(fmt))

print('카운트 다운을 시작합니다')
t.sleep(1) # 1초동안 실행대기
print(5)
t.sleep(1)
print(4)
t.sleep(1)
print(3)
t.sleep(1)
print(2)
t.sleep(1)
print(1)
t.sleep(1)
print(0)

# 할인율 모듈 프로그램
import module.sale as s

# lotto program
from module.Lotto645 import Lotto654

Lotto654()