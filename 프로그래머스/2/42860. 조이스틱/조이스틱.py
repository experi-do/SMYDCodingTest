'''
    A   B   C   D   E
    0   1   2   3   4 
    26  25  24  23  22 
    
    F   G   H   I   J   
    5   6   7   8   9
    21  20  19  18  17
    
    K   L   M   N   O
    10  11  12  13  14
    16  15  14  13  12
    
    P   Q   R   S   T
    15  16  17  18  19
    11  10  9   8   7  
    
    U   V   W   X   Y   Z
    20  21  22  23  24  25
    6   5   4   3   2   1
    
    A   A   A   A   A   A
    0   0   0   0   0   0
    J   E   R   O   E   N
    9   4   -   -  4   13
    -   -  9   12  -   13
    
    51
    두번쨰 글자가 A인 경우와 마지막 글자가 A인 경우, 연속된 A 구해서 적은 쪽 방향으로
    
    jaoon
    
    JAOAAA: 2, 4
    JAAOAAA: 3, 4
    JAAAOAN: 4, 3
    
    len(name) - 1 - a_end
    len(name) - 1 - a_begin
    
    
    AAOAA
    BBAAB
    BBAABBB
    BABAA
    
    
'''
from collections import defaultdict
def solution(name):
    all_A = True
    for i in name:
        if i != 'A':
            all_A = False
            break
    if all_A:
        return 0
            
    answer = 0
    
    char_dict = defaultdict(int)

    char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for i in range(len(char_list)):
        char_dict[char_list[i]] = min(i, 26-i)
    
    for n in name:
        answer += char_dict[n]
        
    print(answer)
    
    move = len(name) - 1
    for i in range(len(name)):
        j = i + 1
        # i 다음부터 연속된 A를 건너뛴다
        while j < len(name) and name[j] == 'A':
            j += 1
        # min(move, 오른쪽 갔다가 되돌아오기, 끝쪽 먼저 갔다가 되돌아오기)
        # "BBABB"
        print(i,j)
        print(move, 2*i+(len(name)-j), i + 2 * (len(name) - j))
        move = min(move, 2 * i + (len(name) - j), i + 2 * (len(name) - j))
        
    print(move)
    
    answer += move
    
    return answer

