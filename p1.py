# coding: utf-8
n = int(input())

for i in range(n):
    line = input()
    a, b = line.split()
    s = int(a, 2) + int(b, 2)
    print(a, b, bin(s)[2:])
