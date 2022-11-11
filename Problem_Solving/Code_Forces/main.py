# n = int(input())
# a = [int(i) for i in input().split()]
# for i in a:
#     if a.count(i) > (n + 1) // 2:
#         print("NO")
#         break
# else:
#     print("YES")


length = int(input())
array = [int(element) for element in input().split()]
for i in array:
    if array.count(i) > (length+1)//2:
        print('NO')
        break

else:
    print('YES')