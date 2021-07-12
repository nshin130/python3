from EMP import EMP
from EMPService import EMPService

emp = EMP(123, 'King', 'Steven', 'steve@king.com', '123-456-789',
               '2003-06-17', 'Ad_PRES', 24000, '', '', 90)
print(emp)

# empsrv = EMPService() # 객체 생성
# emp = empsrv.readEMP() # 매소드 호출
# print(emp)

emp = EMPService.readEMP()  # 객체생성없이 바로 메서드 호출 -> staticmethod 사용
print(emp)

###
# from datetime import datetime
# datetime.now()
# now = datetime(2021,7,12)
# hire = datetime(2003,6,17)
#
# days = now - hire # 근무일수
# print(days)

EMPService.computeDuty(emp)