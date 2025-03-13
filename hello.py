import random
from collections import deque
def ask():
    options = ['버블 정렬']
    print("1.버블 정렬")
    a = int(input("입력해주세요 : "))
    return a


def bubble(l):
    for j in range(len(l)):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                s = l[i]
                l[i] = l[i+1]
                l[i+1] = s
    return l

def dfs(g, s, l):
    if s in l:
        return l
    l.append(s)
    for i in range(len(g)):
        if g[s-1][i]:
            l = dfs(g, i+1, l)
    return l

def bfs(g, q, l):
    while q:
        d = q.popleft()
        for i in range(len(g[d-1])):
            if g[d-1][i] and not(i+1 in l):
                q.append(i+1)
                l.append(i+1)
    return l

def fibo(n):
    for i in range(n):
        if i == 0:
            print(1)
            a = 1
        else:
            print(a)
            a += fibo(a)
            
    return a

#전위순회
def dlr(l, n):
    result = ''
    if len(l) <= n:
        return result
    result += str(l[n])
    result += dlr(l, n*2)
    result += dlr(l, n*2+1)
    return result

#중위순회
def ldr(l, n):
    result = ''
    if len(l) <= n:
        return result
    result += ldr(l, n*2)
    result += str(l[n])
    result += ldr(l, n*2+1)
    return result

#후위순회
def lrd(l, n):
    result = ''
    if len(l) <= n:
        return result
    result += lrd(l, n*2)
    result += lrd(l, n*2+1)
    result += str(l[n])
    return result

#힙 생성 알고리즘

g = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
b = deque([1])
l = [1]
a = bfs(g, b, l)
print(a)

r = bubble([2, 4, 3, 6, 5, 1])
print(r)



