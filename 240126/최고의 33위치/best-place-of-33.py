n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
a = n-2
max = 0
for i in range(a):
    for j in range(a):
        max_now = 0
        for k in range(3):
            for l in range(3):
                max_now += arr[i+k][j+l]
        if max_now >= max: max = max_now
print(max)