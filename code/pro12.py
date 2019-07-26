kk=int(input())
qq=[]
for j in range(0,kk):
    rr=input()
    qq.append(rr)
ss=[]
for k in zip(*qq):
    if(j.count(j[0]==len(j))):
        ss.append(j[0])
    else:
        break
print(''.join(ss))
