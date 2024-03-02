n = int(input())
student_list = []

for i in range(n):
    name, a, b, c = input().split(' ')
    student = [name, int(a), int(b), int(c)]
    student_list.append(student)

student_list.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for score in student_list:
    print(score[0])