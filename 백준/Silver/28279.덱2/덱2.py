from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
que = deque()

for i in range(N):
    ord = list(map(int,input().split()))
    if ord[0] == 1:
        que.appendleft(ord[1])
    elif ord[0] == 2:
        que.append(ord[1])
    elif ord[0] == 3:
        if que:
            print(que.popleft())
        else:
            print('-1')
    elif ord[0] == 4:
        if que:
            print(que.pop())
        else:
            print('-1')
    elif ord[0] == 5:
        print(len(que))
    elif ord[0] == 6:
        if que:
            print('0')
        else:
            print('1')
    elif ord[0] == 7:
        if que:
            print(que[0])
        else:
            print('-1')
    elif ord[0] == 8:
        if que:
            print(que[-1])
        else:
            print('-1')