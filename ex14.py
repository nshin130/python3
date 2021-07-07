#실전예제
stud = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']
stud.sort(reverse=False)
print(stud)

stud.remove('박찬호')
print(f'학생수: {len(stud)}명 \n'
      f'학생: {stud}')

help = stud[:3]
print(help)

stud.append('이병규')
print(stud)

stud.sort(reverse=True)
print(stud)

stud[1] = '정잘남'


