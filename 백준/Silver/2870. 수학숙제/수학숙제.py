import re

t = int(input())

words = []
num_list = []
for _ in range(t):
    word = input()
    words.append(word)
    num= re.findall(r'\d+', word)
    for n in num:
        num_list.append(int(n))

sorted_num_list = sorted(num_list)
for num in sorted_num_list:
    print(num)