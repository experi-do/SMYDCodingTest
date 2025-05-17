def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = commands[i]
        start, end, target = arr[0]-1, arr[1], arr[2]-1
        selected = array[start:end]
        selected.sort()
        answer.append(selected[target])
    return answer
