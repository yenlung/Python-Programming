# coding: utf-8
k = int(input())
line = input()

st = ''.join([str(int(x.isupper())) for x in line])

pattern = ['0'*k, '1'*k]
p0 = ''
p1 = ''

c = True
m = 0


while c:
    p0 = p0 + pattern[m%2]
    p1 = p1 + pattern[(m+1)%2]
    
    if (p0 in st) or (p1 in st):
        m = m + 1
    else:
        c = False
        
print(m*k)
