# 이름 국어 영어 수학을 입력받아 총점 평균 학점을 구하는 프로그램
name = input('이름을 입력하세요 ')
kor = int(input('국어 성적을 입력하세요 '))
eng = int(input('영어 성적을 입력하세요 '))
mat = int(input('수학 성적을 입력하세요 '))
tot = kor + eng + mat
avg = float(tot / 3)
grd = '수' if (avg >= 90) else \
      '우' if (avg >= 80) else \
      '미' if (avg >= 70) else \
      '양' if (avg >= 60) else '가'

print(f'{name} / {kor} / {eng} / {mat} / {tot} / {avg:.2f} / {grd}')
