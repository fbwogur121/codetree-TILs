n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in range(2 * n):
    same = 0
    if i < n:  #가로줄
        for j in range(n - m + 1):  # Fix loop range
            if all(arr[i][j + k] == arr[i][j + k + 1] for k in range(m - 1)):
                same += 1
    else:  #세로줄
        for k in range(n - m + 1):  # Fix loop range
            if all(arr[k + l][i % n] == arr[k + l + 1][i % n] for l in range(m - 1)):
                same += 1

    if same > 0:
        res += 1

print(res)