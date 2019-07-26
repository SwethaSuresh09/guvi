def,deg=map(int,input().split())
ll=list(map(int,input().split()))
q=0
for k in range(0,def):
for l in range(1,def):
if ll[k]+ll[l]==deg and k!=l:
q=1
break
print("yes" if q else "no")
