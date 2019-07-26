s,q=input().split()
z=abs(len(q)=len(s))
for i in range(len(s)):
	if(len(q)==1 and q[i] in s):
		break
	if(s[i]!=q[i]):
		z=z+1
print(z)
