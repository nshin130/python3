# # 헌혈프로그램
# bloodtype = []
# for i in range(10):
#     q = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 \n'
#               'A, B, AB, O: ')
#     bloodtype.append(q)
#
# print(bloodtype)
#
# a = []
# b = []
# ab = []
# o = []
#
# for i in range(10):
#     blood = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요. \n'
#                   'A, B, AB, O:')
#     if blood == 'A' or blood == 'a': a.append(blood)
#     elif blood == 'B' or blood == 'b':b.append(blood)
#     elif blood == 'AB' or blood == 'ab':ab.append(blood)
#     elif blood == 'O' or blood == 'o':o.append(blood)
#
#  print(f'혈액형 수급 현황 \n'
#        f'A형 : {len(a)}\n'
#        f'B형 : {len(b)}\n'
#        f'AB형 : {len(ab)}\n'
#        f'O형 : {len(o)}')

bloods = []
for i in range(10):
    blood = input('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요. \n'
                   'A, B, AB, O:')
    bloods.append(blood)

print('-'*30)
print(f'혈액형 수급 현황')
print('-'*30)
print(f'A형 : {bloods.count("A")}')
print(f'B형 : {bloods.count("B")}')
print(f'AB형 : {bloods.count("AB")}')
print(f'O형 : {bloods.count("O")}')
print('-'*30)
