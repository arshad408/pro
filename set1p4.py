m,j=map(str,input().split())
s=0
if len(m)>len(j):
  m,j=j,m
i=0
while i<len(m):
  s+=(ord(j[i])-ord(m[i]))
  i+=1
for i in range(i,len(j)):
  s+=ord(j[i])-ord('a')+1
print(s)
