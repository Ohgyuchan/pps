def solution(s):
    length = len(s)
    answer = length
    
    # 자르는 개수 : 1 ~ length / 2
    for number in range(1, 1 + length // 2):
        before = s[: number]
        start_idx = number
        score = length
        iter = 0
        
        # 문자열 안에서 잘라가며 반복확인
        while (start_idx + number) <= length:
            now = s[start_idx: start_idx+number]
            if now == before:
                if iter == 0:
                    iter = 1
                iter += 1
                score -= number
            else:
                if iter >= 1:
                    score += len(str(iter))
                    iter = 0
            
            before = now
            start_idx += number
        
        if iter >= 1:
            score += len(str(iter))
        if score < answer:
            answer = score
    
    return answer