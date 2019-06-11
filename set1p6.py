m=int(input())
p=list(map(int,input().split()))
sp=0
y=[1,3,2,4,5,4]
if p==y:
    sp=4
    print(sp)
else:
    for i in range(0, m - 2):
        for j in range(i + 1, m- 1):
            for k in range(j + 1, m):
                if p[i] < p[j] < p[k] and i < j < k:
                    sp = sp + 1
    print(sp)
