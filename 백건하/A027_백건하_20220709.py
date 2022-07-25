def solution(number, k):
    idx = 0
    count = 0 # 지운 숫자의 개수
    
    # 앞에부터 2개씩 비교 / count 꽉차거나 idx가 끝에 도달하면 끝
    while(count < k and idx < len(number)-1):
        
        before = int(number[idx])
        after = int(number[idx+1])
        # 앞 숫자가 작으면 remove
        if before < after:
            number = number[: idx] + number[idx+1: ]
            count += 1
            # 다시 전부터 비교하기 위해 i -= 1
            if idx != 0:
                idx -= 1
        else:
            idx += 1
    
    # 못지운 개수 만큼 오른쪽에서 자르기
    left = k - count
    
    if left != 0:
        number = number[: len(number)-left]

    return number
