import sys

x=0
y=0
for line in sys.stdin:
    d = {}
    f=0
    g=0
    for c in line:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in d:
        if not f and d[c] == 2:
            f = 1
        if not g and d[c] == 3:
            g = 1
        if f and g: break
    if f: x+=1
    if g: y+=1
print x*y