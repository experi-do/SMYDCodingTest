'''
    가로 변 수 + 세로 변 수 + 4 == brown
'''

def getLength(yellow):
    possibleLength = [(yellow//1, 1)]
    for i in range(1, (yellow//2)+1):
        if yellow % i == 0:
            possibleLength.append((max(i, yellow//i), min(i, yellow//i)))
    return list(set(possibleLength))
        

def solution(brown, yellow):
    answer = 0
    
    yellowLength = getLength(yellow)
    for yel in yellowLength:
        if (2 * sum(yel) + 4) == brown:
            return [yel[0]+2,yel[1]+2]