def func1(n, m, arr):  # ㄱ자 3칸
    res = 0
    for i in range(n-1):
        for j in range(m-1):
            p=arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]
            p -= min(arr[i][j],arr[i][j+1],arr[i+1][j],arr[i+1][j+1])
            if p>res: res=p
    return res
    
def func2(n, m, arr):  # 1자 3칸
    res = 0
    for k in range(n+m):
        if(k<n):    
            for i in range(n): # 가로줄
                for j in range(m-2):
                    p = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                    if p>res: res=p
        else:  #세로줄
            q = k-n
            for l in range(m):
                for t in range(n-2):
                    z = arr[t][l]+arr[t+1][l]+arr[t+2][l]
                    if z>res: res = z
    return res

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]

print(max(func1(n, m, arr),func2(n, m, arr)))