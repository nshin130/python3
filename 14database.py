# sqlite 를 이용한 데이터 베이스 활용하기

import sqlite3

# 데이터 조회

# DB connect
conn = sqlite3.connect('/Users/nara/sqlite3/nshin.db')

# 접속후 커서를 가져옴
cur = conn.cursor()

# 질의문 작성
sql = 'select pcode, pname, price, amount from product'

# 질의문 실행후 결과 집합 가져오기
# 결과 집합은 리스트 형태로 저장
cur.execute(sql)
rows = cur.fetchall()

# 리스트의 내용 출력하기
for row in rows:
    print(row[0], row[1], row[2], row[3])

# 리스트의 내용 출력하기 II
# 리스트를 컬럼명으로 출력하려면 커서모드는 dictCursor 이용
# 단 sqlite3은 미지원
# for row in rows:
#     print(row['pcode'], row['pname'], row['price'], row['amount'])

# 작업종료
cur.close()
conn.close()

# mysql를 이용한 데이터베이스 활용하기
import pymysql

conn = pymysql.connect(host='bigdata.ckwuhzosrgyo.ap-northeast-2.rds.amazonaws.com',
                       charset='utf8', user='playground', password='bigdata2020', db='playground')

# 결과 집합 출력시 dict형식으로 리스트를 다룰 수 있음
# dictcursor 사용 -> 컬럼명으로 resultset 제어
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from EMPLOYEES'
cursor.execute(sql)
rows = cursor.fetchall()

cursor.close()
conn.close()

for row in rows:
    print(row['EMPLOYEE_ID'], row['FIRST_NAME'], row['LAST_NAME'])


# 직책이 IT_PROG인 사원들의 사번 성 입사일을 출력하는 코드 작성
import pymysql

conn = pymysql.connect(host='bigdata.ckwuhzosrgyo.ap-northeast-2.rds.amazonaws.com',
                       charset='utf8', user='playground', password='bigdata2020', db='playground')

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = ' select EMPLOYEE_ID, LAST_NAME, HIRE_DATE FROM EMPLOYEES WHERE JOB_ID = "IT_PROG" '

cursor.execute(sql)
rows = cursor.fetchall()

cursor.close()
conn.close()

for row in rows:
    print(row['EMPLOYEE_ID'], row['LAST_NAME'], row['HIRE_DATE'])

# 30번 부서의 사원수를 조회하는 코드 작성
conn = pymysql.connect(host='bigdata.ckwuhzosrgyo.ap-northeast-2.rds.amazonaws.com',
                       charset='utf8', user='playground', password='bigdata2020', db='playground')

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = ' select count(LAST_NAME) cnt from EMPLOYEES where DEPARTMENT_ID = "30" '

cursor.execute(sql)
rows = cursor.fetchone()

cursor.close()
conn.close()

# 단일값이므로 for문 없이 바로 출력
print(rows[0])

print(rows['cnt'])

for row in rows:
    print(row)

# 데이터 삽입

import sqlite3

# DB connect
conn = sqlite3.connect('/Users/nara/sqlite3/nshin.db')

# 접속후 커서를 가져옴
cur = conn.cursor()

# 질의문 작성
pcode = '12345'
pname = '에어컨'
price = 35000
amount = 10
sql = ' insert into product values ' \
      f'("{pcode}","{pname}","{price}","{amount}") '

# 질의문 실행
cur.execute(sql)

# 질의문 작성 II 9 - sqlite3 미지원
sql = ' insert into product values (%s, %s, %d, %d) '
param = (pcode, pname, price, amount)

# 질의문 실행 II
cur.execute(sql, param)


# 실행한 내용을 서버에 반영
conn.commit()

# 작업종료
cur.close()
conn.close()

# 이름 국어 영어 수학을 입력 받아 sungjuk 테이블에 저장

import pymysql

conn = pymysql.connect(host='bigdata.ckwuhzosrgyo.ap-northeast-2.rds.amazonaws.com',
                       charset='utf8', user='playground', password='bigdata2020', db='playground')

cur = conn.cursor(pymysql.cursors.DictCursor)

name = input('이름은?')
kor = input('국어는?')
eng = input('영어는?')
mat = input('수학은?')

sql = ' insert into sungjuk (name, kor, eng, mat) ' \
      ' values (%s, %s, %s, %s) '
param = (name, kor, eng, mat)

cnt = cur.execute(sql, param)
print( '입력한 데이터 건수: ', cnt)

conn.commit()

cur.close()
conn.close()



