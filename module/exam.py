# 시험 통과 여부

def examResult(kor, eng, mat):

    tot = kor + eng + mat
    avg = tot / 3
    isPass = '불합격'

    isAll60 = avg >= 60
    is40 = kor >= 40 or eng >= 40 or mat >= 40

    if isAll60 and is40:
        isPass = '합격'

    # 파이썬에서 함수의 리턴값으로 2개이상 지정 가능
    return tot, avg, isPass



    # for i in (1,3+1):
    #     scores += score
    #     tot += score[i]
    #     avg = tot / [i]
    #
    #     if avg >= 60:
    #         if score[i] >= 40:
    #             print(f'총점:{tot} 평균:{avg} 합격여부:Pass')
    #     else:
    #         print(f'총점:{tot} 평균:{avg} 합격여부:Fail')