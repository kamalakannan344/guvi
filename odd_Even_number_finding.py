x=int(input())
y=list(map(int,input().split()[:x]))
for i in range (0,x):
  if (i%2==0) and (y[i]%2!=0):
    print(y[i])
  elif (i%2!=0) and (y[i]%2==0):
    print(y[i])
