from itertools import permutations

def isPrime(num):
    sqrt_num = int(num**(0.5))
    for i in range(2,sqrt_num+1):        
        if num % (i) == 0:
            return False
        
    return True
                

def solution(numbers):
    answer = 0
    
    num_list = []
    for n in str(numbers):
        num_list.append(int(n))
        
    total_list = []
    for i in range(len(numbers)):
        total_list += permutations(num_list, i+1)
        
    final_list = []
    for num in total_list:
        a = ''
        for n in num:
            a += str(n)
        if int(a) not in final_list:
            if int(a) > 1 and isPrime(int(a)):
                final_list.append(int(a))
                
    return len(final_list)