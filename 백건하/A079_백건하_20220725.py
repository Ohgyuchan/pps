def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        dividedArray = array[commands[i][0]-1: commands[i][1]]
        dividedArray.sort()
        answer.append(dividedArray[commands[i][2]-1])
    return answer