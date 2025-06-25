'''
{5} -> N==number이면 return 1
{55}
{555}
{5555}
{55555}
{555555}
{5555555}
{55555555}

작 -> 큰
이중 for문으로 


'''
def solution(N, number):
    answer = -1
    if N == number:
        return 1
    
    s = [set() for _ in range(8)]
    for idx, x in enumerate(s, start=1):
        x.add(int(str(N)*idx))
        
    # for i in range(8):
    #     print(s[i])
        
    for i in range(1, 8):
        for j in range(i):
            print('****')
            print(i, j)
            print(s[j])
            print(s[i-j-1])
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+1
            break
    return answer