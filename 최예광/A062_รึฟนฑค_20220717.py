def solution(a, b):
    dcount = 0
    day31 = [1,3,5,7,8,10]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    for i in range(a)[1:]:
        if i in day31:
            dcount += 31
        elif i == 2:
            dcount += 29
        else:
            dcount += 30
    dcount += b - 1
    return day[dcount%7]