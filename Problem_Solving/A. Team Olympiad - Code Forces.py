"""A. Team Olympiad - Code Forces"""

n = int(input())
skills = list(map(int, input().split()))
prog = skills.count(1) # num programmers
math = skills.count(2)  # num mathematitians
phys = skills.count(3)  # num Physical Education Students
k = min(prog, math, phys) # Min of all to know how many teams we can form
print(k) # number of teams
idx1,idx2,idx3=[],[],[] # 3 lists
# collect every kind in a list 
for i in range(len(skills)):
    if skills[i]==1:
        idx1.append(i+1)
    if skills[i]==2:
        idx2.append(i+1)
    if skills[i]==3:
        idx3.append(i+1)
# Loop over the number of teams and print a team formed from 3 diff students
for i in range(k):
    print(idx1[i], idx2[i], idx3[i])