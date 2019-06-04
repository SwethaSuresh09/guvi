yyr=int(input())
if(((yyr%4==0) or (yyr%400)==0) and (yyr%100!=0)):
    print("yes")
else:
    print("no")
