def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    
    
    return participant[-1]
participation = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
solution(participation, completion)