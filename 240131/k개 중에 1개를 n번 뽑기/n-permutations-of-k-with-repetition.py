K, M = map(int, input().split())

a = []
def choose(cnt):
    if cnt == M+1 :
        print(*a)
        return

    for i in range(1,K+1):
        a.append(i)
        choose(cnt + 1)
        a.pop()

choose(1)