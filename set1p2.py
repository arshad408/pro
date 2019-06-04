from itertools import combinations
g,n=map(int,input().split())
p=len(str(g))
m=list(combinations(str(g),p-n))
m=sorted(m)
print("".join(m[0]))
