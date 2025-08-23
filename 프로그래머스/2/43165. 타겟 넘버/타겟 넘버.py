def backtrack(numbers, target, idx, node_list=[]):
    global answer
    if len(node_list) == len(numbers) and sum(node_list) == target:
        answer += 1
        return
    if idx == len(numbers):
        return

    mult = [-1, 1]

    for i in range(2):

        if visited[idx][i]:
            continue

        visited[idx][i] = True
        node_list.append(numbers[idx] * mult[i])
        backtrack(numbers, target, idx + 1, node_list)
        node_list.pop()
        visited[idx][i] = False


def solution(numbers, target):
    global visited, answer
    visited = [[False for _ in range(2)] for _ in range(len(numbers))]

    answer = 0

    backtrack(numbers, target, 0, [])

    return answer