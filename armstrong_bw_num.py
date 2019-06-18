a,b=map(int,input().split())
for i in range(a+1,b):
    c=0
    d=i
    while(d>0):
        e=d%10
        d=d//10
        f=e**3
        c=c+f
    if(i==c):
        print(c,end=' ')
