m=int(input())
p=[int(i) for i in input().split()]
sp=0
for i in range(m):
	for j in range(i):
		if p[j]<p[i]:
			sp+=p[j]
print(sp)
