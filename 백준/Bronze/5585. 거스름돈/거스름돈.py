n = int(input())
money = 1000 - n
answer = 0
cnt = 0
while (money > 0):
    cnt += 1
    if (money // 500 > 0):
        answer += (money // 500)
        money -= 500 * (money // 500)
    elif (money // 100 > 0):
        answer += (money // 100)
        money -= 100 * (money // 100)
    elif (money // 50 > 0):
        answer += (money // 50)
        money -= 50 * (money // 50)
    elif (money // 10 > 0):
        answer += (money // 10)
        money -= 10 * (money // 10)
    elif (money // 5 > 0):
        answer += (money // 5)
        money -= 5 * (money // 5)
    elif (money // 1 > 0):
        answer += money
        money = 0
print(answer)