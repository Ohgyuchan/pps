def solution(citations):
    answer = 0
    count = 0
    length = len(citations)
    
    citations.sort(reverse = True)
    print(citations)
    
    for i in range(length):
        if i+1 > citations[i]:
            break
        count = i+1

    answer = count
    
    return answer