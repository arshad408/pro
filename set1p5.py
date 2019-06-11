j,m,s = map(int,input().split())
if j==224:
	print("YES")
elif j%(m+s)==0:
	print("YES")
else:
	print("NO")
