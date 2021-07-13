# 문자열은 문자들의 리스트와 유사
# 따라서 리스트 슬라이싱을 통해 문자열내 개별 문자를 추출할 수 있음

# '파이썬은완전재미있어요' 라는 문자열에서
# 홀수 위치에 있는 문자를 #로 출력하는 코드 작성

str = '파이썬은완전재미있어요'
slen = len(str)
for i in range(0, slen):
    if i % 2 == 0:
        print(str[i], end='')
    else:
        print('#', end='')
print()


# 문자열 함수
# 대소문자 변환
str = 'Python is Easy. 그래서 programming이 재미있어요'
str.lower()
str.upper()
str.swapcase()
str.title()

# 문자열 찾기
str = '파이썬 공부는 즐겁습니다 물론 모든 공부가 다 재미있지는 않죠^^'

str.count('공부')     # 특정문자열 포함 갯수
str.find('공부')      # 문자열을 찾은 위치 (왼쪽 기준)
str.find('공부', 5)   # 특정인덱스를 시작으로 문자열을 찾은 위치 (왼쪽 기준)
str.find('공부', str.find('공부')+1)
str.find('없다')      # 찾지 못하는 경우: -1
str.rfind('공부')     # 문자열을 찾은 위치 (오른쪽 기준)

str.index('공부')
str.index('공부', 5)
str.rindex('공부')
str.index('없다')     # 찾지 못하는 경우: 오류

str.startswith('파이썬')        # 특정문자열로 시작하는지 여부
str.startswith('파이썬', 10)    # 특정인덱스 이후로 특정 문자열로 시작하는지 여부
str.startswith('물론', 14)
str.endswith('^^')             # 특정문자열로 끝나는지 여부

# 문자열 내 공백 다루기
str = '  파  이  썬  '
str.strip()         # 공백제거: 매개변수 없음
str.rstrip()        # 오른쪽 공백제거
str.lstrip()        # 왼쪽 공백제거

str = '--파---이---썬--'
str.strip('-')      # 지정문자 제거: 매개변수로 제거할 문자 지정
str.rstrip('-')
str.lstrip('-')

str = '<<파 << 이 >> 썬>>'
str.strip('<>')      # 지정문자들 제거: 매개변수로 제거할 문자열 지정
str.lstrip('<>')
str.rstrip('<>')

str = '열심히 파이썬 공부중~'
str.replace('파이썬','python')   # 지정한 문자열을 새로운 문자열로 바꿈

str = '  파  이  썬  '
str.replace(' ','')

str = '--파--이--썬--'
str.replace('-','')

str = '<<파 << 이 >> 썬>>'
str = str.replace('<', '')
str = str.replace('>', '')
str.replace(' ','')

# 문자열 분리 결합
str = '혜교,98,95,77'     # 구분기호로 문자열 분리후 리스트로 저장
str.split(',')

str = '혜교|98|95|77'
str.split('|')

str = '혜교\r\n98\r\n95\r\n77'
str.split('\r\n')       # 줄바꿈 기호 기준 문자열 분리
str.splitlines()


str = ['혜교','98','95','77']
','.join(str)           # 리스트의 각 항목을 구분기호로 결합

result = ''             # 조인을 사용하지 않은 경우
for s in str:
    result += s + ','

# 객체를 특정 함수에 일괄적으로 적용하기
# map(적용할 함수명, 대상객체)
str = ['123', '456', '789'] # 문자열 -> 숫자열

# map을 사용하지 않은 경우
nums = []
for s in str:
    nums.append(int(s))

# map을 사용한 경우
nums = list(map(int,str))

# 문자열 정렬하기

# 특정 문자로 채우기

# 문자열 구성 파악하기

# 입력한 값이 영어/한글이면 '글자', 숫자면 '숫자', 섞여있으면 '글자+숫자',
# 그 외 나머지 문자면 '모르겠습니다' 라고 출력하는 프로그램

msg = input('문자를 입력해주세요')
msg = msg.replace(' ','')

result = ''
if msg.isalpha():
    result = '글자입니다'

elif msg.isdigit():
    result ='숫자입니다'

elif msg.isalnum():
    result = '글자+숫자입니다'

else:
    result = '모르겠습니다'

print(result)