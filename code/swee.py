x=int(input())
y=0
t=[]
for x in range(1,x+1):
    t.append(x)
for x in range(len(t)):
    for x in range(x+1,len(t)):
        y+=1
print(y)
