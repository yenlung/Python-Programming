# coding: utf-8
line = input().split()
a, b, c = map(int, line)
if a != 0:
    a = 1
if b != 0:
    b = 1
if c != 0:
    c = 1

fail = True
if (a & b == c):
    print("AND")
    fail = False
if (a | b == c):
    print("OR")
    fail = False
if (a ^ b == c):
    print("XOR")
    fail = False
if fail:
    print("IMPOSSIBLE")
