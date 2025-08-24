from collections import defaultdict

def solution(gems):
    num_unique_gems = len(set(gems))
    n = len(gems)

    answer = [0, n - 1]

    start = 0
    gem_counts = defaultdict(int)

    for end in range(n):
        gem_counts[gems[end]] += 1

        while len(gem_counts) == num_unique_gems:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            gem_counts[gems[start]] -= 1
            if gem_counts[gems[start]] == 0:
                del gem_counts[gems[start]]

            start += 1

    return [answer[0] + 1, answer[1] + 1]