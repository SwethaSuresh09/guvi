z11=int(input())
z22=list(map(int,input().split()))
z33=int(len(z22)/2)
if sum(z22[:z33])//len(z22[:z33])==sum(z22[z33:])//len(z22[z33:]):
    print('yes')
else:
    print('no')
