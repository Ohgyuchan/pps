def solution(n, lost, reserve):
    
    student = [1 for _ in range(n+1)]
    
    for one in lost:
        student[one] -= 1
    
    for one in reserve:
        student[one] += 1
        
    for i in range(1, n+1):
        if i == n:
            if student[i-1] == 2:
                student[i] = 1
                student[i-1] = 1
            break
        
        if student[i] == 0:
            if student[i-1] == 2:
                student[i] = 1
                student[i-1] = 1
            elif student[i+1] == 2:
                student[i] = 1
                student[i+1] = 1
                
    return n - student.count(0)