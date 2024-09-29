import math
for t in range(int(input())):
    s = input()
    tong = 0
    check = True
    for i in range(len(s)-1):
        if abs(int(s[i+1]) - int(s[i])) != 2:
            check=False
            break
    for i in s:
        tong+=int(i)
    if tong%10 != 0:
        check=False
    if check:
        print('YES')
    else:
        print('NO')