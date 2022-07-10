s=input()
x=s.split(" ")
a=len(x)
if a==2:
    print(min(x[0]),max(x[1]))
else:
    print(min(x[0]),max(x[a-2]))
    