# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# 어떤 입력값을 주면 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 다른 사람과의 협업시 코드가 섞이지 않게
# 하기 위한 목적도 있음 - 모듈

def startSensor():
    print('온도센서 작동을 시작합니다')

def stopSensor():
    print('온도센서 작동을 중지합니다')

startSensor()
stopSensor()

# 노트북 파우치 인치 변환 1cm => 0.393701 inch
def convertcm2in(cm):
    print(f'{cm * 0.393701:2f}')
    # return cm * 0.393701

cm = int(input('파우치 길이를 입력하세요'))
convertcm2in(cm)

# print(convertcm2in(cm)) -> return 쓴경우

# 이동거리 계산 함수
def computeDistance(time, speed):
    print(f'이동거리는 {time * speed}km 입니다')

speed = float(input('이동 속도는?'))
time = float(input('이동 시간은?'))
computeDistance(time, speed)

