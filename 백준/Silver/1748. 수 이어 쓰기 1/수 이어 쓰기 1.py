n = int(input())

# str_num = ''
# for i in range(1, n+1):
#     str_num += (str(i))
# print(len(str_num))

str_n = str(n)
len_n = len(str_n)
ans = 0
memo = [0]*len_n
for i in range(len_n):
    memo[i] = 9 * 10**(i) * (i+1)
# print(memo)

for i in range(len_n):
    if i != len_n-1:
        ans += memo[i]
        # print(memo[i])
    else:
        temp = (i+1)*(n-10**(i)+1)
        # print(f'temp: {temp}')
        ans += temp
        pass
print(ans)


# for i in range(len_n, 0, -1):
#     print(10**(i-1))


'''
125
3자리: 100~999
2자리: 10~99
1자리: 1~9

9 90 900

1 2 3 4 5 6 7 8 9
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29

'''