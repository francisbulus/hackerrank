for _ in range(int(input())):
    n, k = map(int, input().strip().split(" "))
    a = list(map(int, input().strip().split(" ")))
    b = list(map(int, input().strip().split(" ")))
    a = list(sorted(a))
    b = list(reversed(sorted(b)))
    flag = True
    for i in range(n):
        if a[i] + b[i] < k:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")