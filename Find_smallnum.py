x=int(input())
y=list(map(int,input().split()[:x]))
y.sort()
print(y[0])
