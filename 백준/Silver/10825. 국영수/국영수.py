import sys
input = sys.stdin.readline


T = int(input())
l = [list(input().split()) for _ in range(T)]

l.sort(key=lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(T):
    print(l[i][0])
