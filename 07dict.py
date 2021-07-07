# Dictionary
ages = {'박찬호':48, '박지성':40, '박세리':50, '이승엽':43}
type(ages)

person = {'이름':'홍길동', '나이':25, '몸무게':88.8, '주소':'서울 종로구 삼일대로', '취미':['승마', '하이킹', '음악듣기']}

sungjuk = {'C/C++':'A', 'Java':'B+', '네트워킹':'C', '보안':'A+', '해킹':'F', '시스템':'C+'}
print(sungjuk)

# 홍길동의 나이와 취미 조회
person['나이']
person['취미']

# 홍길동의 혈액형 추가
# dict에 새로운 항목을 추가할떄는
# 새로운 키와 값으로 구성해야 함
person['혈액형'] = 'A'
person

# dict에 기존 키와 값으로 구성한 항목을
# 추가하려 하면 기존키에 값이 적용됨
person['혈액형'] = 'O'

# dict 에서 항목 삭제 : pop()
person.pop('몸무게')

dellist = ['나이', '취미']
for key in dellist:
    person.pop(key)

# dict 모든 항목 출력
person = {'이름':'홍길동', '나이':25, '몸무게':88.8, '주소':'서울 종로구 삼일대로', '취미':['승마', '하이킹', '음악듣기']}

for key in person.keys():
    print(person[key])

# dict 키와 값 모두 가져오기 : items
person.items()

for k,v in person.items():
    print(k,v)

# 중간고사 성적 관리 프로그램 만들기
midterm = {'C/C++':'A', 'Java':'B+', '모바일':'C', '보안':'A+', '해킹':'F', '시스템':'C+'}

midterm['Java']
midterm['시스템']

midterm['Python']='A'
midterm['OS']='A+'
midterm

midterm['Java'] ='F'
midterm['시스템'] ='A'

midterm.items()
for k,v in midterm.items():
    print(f'{k}: {v}')

# 딕셔너리 for 축약문
# { 키/값 표현식 for 키, 값 in zip(반복가능객체1, 반복가능객체2) }

# 이름과 성적 리스트를 dict 객체로 재생성하세요
name = ['혜교', '지현', '수지'] # key
grd = ['수', '양', '미'] # value
sj = {}

# 반복문 x
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

# 반복문 o
for i in range(3):
    sj[name[i]] = grd[i]

# dict comprehension
sj2 = {key: val for key, val in zip(name, grd)}

# zip: 여러개의 데이터를 하나로 합쳐서
# iterable한 객체로 생성해 줌 - 개별객체는 튜플로 반환
for pair in zip(name, grd):
    print(pair)

