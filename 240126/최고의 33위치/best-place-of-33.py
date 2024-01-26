n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
a = n-2
max = 0
for i in range(a):
    for j in range(a):
        max_now = 0
        for a in range(3):
            for b in range(3):
                max_now += arr[i+a][j+b]
        if max_now >= max: max = max_now
print(max)