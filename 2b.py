import sys

ids = []
for line in sys.stdin:
    ids += line,

l = len(ids)
x = len('bvhfajcnyoqkudzrpgsoeimtkj')

for i in range(l):
    for j in range(l):
        if i <= j:
            continue
        diff = 0
        p = -1
        for k in range(x):
            if ids[i][k] != ids[j][k]:
                if diff:
                    break
                else:
                    diff = 1
                    p = k
        else:
            if diff:
                m = list(ids[i])
                m.pop(p)
                print ''.join(m)

