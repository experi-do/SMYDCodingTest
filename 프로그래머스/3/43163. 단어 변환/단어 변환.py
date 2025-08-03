from collections import defaultdict, deque
def solution(begin, target, words):
    dic = defaultdict(list)
    
    if target not in words:
        return 0
    
    words.append(begin)
    lenOfWord = len(begin)
    for word in words:
        for word2 in words:
            if word != words:
                cnt = 0
                for i in range(lenOfWord):
                    if word[i] != word2[i]:
                        cnt += 1
                if cnt == 1:
                    dic[word].append(word2)
    print(dic)
    visited = defaultdict(bool)
    for k in dic.keys():
        visited[k] = False
    
    queue = deque([])
    queue.append((begin, 0))
    visited[begin] = True
    
    
    while queue:
        word, cnt = queue.popleft()
        print(f'current word: {word}, current cnt: {cnt}')
        if word == target:
            return cnt
        
        for w in dic[word]:
            if visited[w] == False:
                queue.append((w, cnt+1))
                visited[w] = True
    
'''
hit
hot
dot lot
dog / log
cog / cog

'''
    
    
    
# from collections import defaultdict, deque
# def solution(begin, target, words):
#     answer = 0
#     dic = defaultdict(list)
    
#     if target not in words:
#         return answer
    
#     words.append(begin)
#     for word in words:
#         for word2 in words:
#             if word != words:
#                 cnt = 0
#                 for i in range(3):
#                     if word[i] != word2[i]:
#                         cnt += 1
#                 if cnt == 1:
#                     dic[word].append(word2)
#     print(dic)
#     visited = defaultdict(bool)
#     for k in dic.keys():
#         visited[k] = False
    
#     stack = deque([])
#     stack.append(begin)
#     visited[begin] = True
    
#     while stack:
#         word = stack.pop()
#         print(f'current word: {word}')
#         if word == target:
#             return answer 
#         answer += 1
        
#         for w in dic[word]:
#             if visited[w] == False:
#                 stack.append(w)
#                 visited[w] = True
    