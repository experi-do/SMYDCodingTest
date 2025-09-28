import sys

s = sys.stdin.readline().strip()

a_cnt = s.count("a")

s = s+s

min_ans = sys.maxsize

for i in range(len(s)-a_cnt):
    window = s[i:i+a_cnt]
    min_ans = min(min_ans, window.count("b"))
    
print(min_ans)