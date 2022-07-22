def solution(board, moves):
    answer = 0
    a = []
    
    for move in moves:
        for b in board:
            if b[move-1] != 0:
                a.append(b[move-1])
                b[move-1] = 0
                break

        if len(a) >= 2 and a[-1] == a[-2]:
            answer += 2
            a = a[:-2]
            
    return answer