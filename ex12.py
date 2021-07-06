# 열차 교차시간

train1 = 10
train2 = 25
train3 = 30

for i in range(1, 540+1): # 분 단위로 고침 9시간 = 540분
    # 분을 시간으로 분리해서 출력
    hour = (i // 60) + 9
    min = i % 60

    if i % train1 == 0 and i % train2 == 0:
        print(f'train1 and train2 bumped! {hour}시 {min}분')
    elif i % train2 == 0 and i % train3 == 0:
        print(f'train2 and train3 bumped! {hour}시 {min}분')
    elif i % train3 == 0 and i % train1 == 0:
        print(f'train3 and train1 bumped! {hour}시 {min}분')