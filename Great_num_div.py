x,y=map(int,input().split())
z=[]
for i in range (1,max(x,y)+1):
  if(x%i==0 and y%i==0):
    z.append(i)
print(max(z))
