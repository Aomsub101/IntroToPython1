number = int(input())
list_num = list(map(int, input().split()))

for i in range(len(list_num) - 1):
    if list_num[i] * list_num[i + 1] > 0:
        print("Yes")
        break
else:
    print("No")
