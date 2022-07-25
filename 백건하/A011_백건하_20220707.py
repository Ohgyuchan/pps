def solution(N, stages):
    user = [] # 해당 스테이지에 머무는 user 수
    
    for num in range(1, N+2):
        user.append(stages.count(num))
    
    lose_rates = [] # 실패율
    for num in range(len(user)-1):
        dodal = sum(user[num:])
        lose = user[num]
        if dodal != 0:
            lose_rates.append([num + 1, lose / dodal])
        else:
            lose_rates.append([num + 1, 0])
    
    lose_rates.sort(key = lambda x: x[1], reverse = True)
    
    answer = []
    for one in lose_rates:
        answer.append(one[0])
    
    return answer