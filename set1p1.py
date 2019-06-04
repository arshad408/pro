m=input()
m=int(m)
j=[]
for i in range(0,m):  
    m1=input()
    j.append(m1)
k=[]
for i in zip(*j):
    if i.count(i[0])==len(i): 
        k.append(i[0])
    else:
        break
print(''.join(k))
