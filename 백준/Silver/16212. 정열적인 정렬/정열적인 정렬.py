import sys
input = sys.stdin.readline


T = int(input())
l = list(map(int, input().split()))
l.sort()

for i in l:
    print(i,end=' ')
