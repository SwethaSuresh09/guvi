los=int(input())
mos=list(map(int,input().split()))
mos.sort(reverse=True)
b00=0
d1=0
resu=[]
for x in range(0,los,2):
    b00=b00+mos[x]
for y in range(1,los,2):
    d1=d1+mos[y]
resu.append([b00,d1])
for x in resu:
    print(x[0] if x[0]>x[1]) else x[1])
