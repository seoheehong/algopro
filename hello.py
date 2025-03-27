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

def sh(s, l, n, m):
    def add(p, q):
        s = set()
        if 0 < p < n-1:
            if l[p+1][q] == 1:
                s.add((p+1, q))
                l[p+1][q] = 2
            if l[p-1][q] == 1:
                s.add((p-1, q))
                l[p-1][q] = 2
        if p == 0:
            if l[p+1][q] == 1:
                s.add((p+1, q))
                l[p+1][q] = 2
        if p == n-1:
            if l[p-1][q] == 1:
                s.add((p-1, q))
                l[p-1][q] = 2
        if 0 < q < m-1:
            if l[p][q+1] == 1:
                s.add((p, q+1))
                l[p][q+1] = 2
            if l[p][q-1] == 1:
                s.add((p, q-1))
                l[p][q-1] = 2
        if q == 0:
            if l[p][q+1] == 1:
                s.add((p, q+1))
                l[p][q+1] = 2
        if q == m-1:
            if l[p][q-1] == 1:
                s.add((p, q-1))
                l[p][q-1] = 2
        return s
    sl = set()
    for i in s:
        r = add(i[0], i[1])
        sl = sl.union(r)
    for i in range(n):
        print(*l[i], sep = '')
    print('')
    if (n-1, m-1) in sl:
        return 0
    sh(sl, l, n, m)

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

# 선택 정렬
def select(l):
    
    for i in range(len(l)):
        m = min(l)
        l[i], m = m, l[i]
    return l

#힙 생성 알고리즘
'''
g = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
b = deque([1])
l = [1]
a = bfs(g, b, l)
print(a)

r = bubble([2, 4, 3, 6, 5, 1])
print(r)
'''
def main():
    l = input()
    s = l.split()

    if s[0] == 'help':
        print("설명")
        return 1
    
    if s[0] == 'bubble':
        if len(s) != 2:
            print('다시 입력해주세요')
            return 1
        l = []
        for i in range(int(s[1])):
            l.append(random.randint(1, int(s[1])))
        print(l)
        a = bubble(l)
        print(a)
        return 1
    
    if s[0] == 'bfs':
        sett = {(0, 0)}
        data = ['''101111
101010
101011
111011''', '''110110
110110
111111
111101''', '''1011111
1110001
1000001
1000001
1000001
1000001
1111111''']
        if s[1] == '1':
            n = 4
            m = 6
            l = []
            for i in data[0].split('\n'):
                l.append(list(i))
            l = [[int(i) for i in ll] for ll in l]
        
        if s[1] == '2':
            n = 4
            m = 6
            l = []
            for i in data[1].split('\n'):
                l.append(list(i))
            l = [[int(i) for i in ll] for ll in l]
        
        if s[1] == '3':
            n = 7
            m = 7
            l = []
            for i in data[2].split('\n'):
                l.append(list(i))
            l = [[int(i) for i in ll] for ll in l]

        sh(sett, l, n, m)
        return 1

            
    

    if s[0] == 'end':
        print("종료")
        return 0

    print('다시 입력해주세요')
    return 1
    

a = main()
while a:
    a = main()



