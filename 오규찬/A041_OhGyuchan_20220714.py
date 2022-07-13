def solution(s):
    answer = ''
    ss = s.split(' ')
    for i in ss :
        answer += i.capitalize()
        if i != ss[-1] :
            answer += ' '
    return answer