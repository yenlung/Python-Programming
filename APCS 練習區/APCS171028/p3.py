# coding: utf-8
n = int(input())

G = {}
V = set(range(1, n+1))

for i in range(n):
    line = input().split()
    if int(line[0]):
        nodes = set(map(int, line[1:]))
        G[i+1] = nodes
        V = V - nodes
    else:
        G[i+1] = []
        V = V - {i+1}

def h(v):
    if G[v] == []:
        return 0
    return max(map(h, G[v])) + 1

H = sum(map(h, G.keys()))
print(V.pop())
print(H)
