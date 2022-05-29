def digit(n):
    c=0
    while(n!=0):
        c+=1
        n//=10
    return c
n=int(input())
if(digit(n)==10 ):
    print('Valid')
else:
    print('Invalid')