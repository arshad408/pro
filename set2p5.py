q=int(input())
r=list(map(int,input().split()))
f=g=[]
for i in range(0,q):
    f=list(bin(r[i]))
    f=f[2:]
    g.append(f)
g=sorted(g)
g=g[::-1]
for i in range(0,q):
    b=1
    z=0
    for j in range(len(g[i])-1,-1,-1):
        z=z+(int(g[i][j])*b)
        b=b*2
    print(z)
