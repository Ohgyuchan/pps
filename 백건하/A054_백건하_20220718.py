def solution(board, moves):
    length = len(board)
    
    l = [[] for _ in range(length)]
    for r in range(length-1, -1, -1):
        for c in range(length):
            val = board[r][c]
            if val != 0:
                l[c].append(val)
    print(l)
    stack = []
    count = 0
    for one in moves:
        if l[one-1]:
            stack.append(l[one-1].pop())
            stack_length = len(stack)
            if stack_length > 1:
                if stack[stack_length-1] == stack[stack_length-2]:
                    stack.pop()
                    stack.pop()
                    count += 2
    
    return count