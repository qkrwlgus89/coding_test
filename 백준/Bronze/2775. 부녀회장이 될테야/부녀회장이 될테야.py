T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    jumin = [i for i in range(1, n+1)]

    for floor in range(k):
        for i in range(1, n):
            jumin[i] = jumin[i] + jumin[i-1]

    print(jumin[n-1])