z,w=map(int,input().split())
t=list(map(int,input().split()))
q=0
for x in range(0,z):
    for y in range(1,z):
        if t[x]+t[y]==w and x!=y:
            q=1
            break
print("yes" if q else "no")
