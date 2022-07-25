def solution(array, commands):
    answer = []
    cases = len(commands)
    
    for command in commands :
        i, j, k = command[0], command[1], command[2]
        a = array[i-1:j]
        answer.append(sorted(a)[k-1])
        
    return answer