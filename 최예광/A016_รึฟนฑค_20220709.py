def solution(people, limit):
    heavy = len(people)-1
    i = 0
    count = 0
    people.sort()
    while i <= heavy:
        sum = people[i] + people[heavy]
        if sum <= limit:
            i += 1
        heavy -= 1
        count += 1
    
    return count
        