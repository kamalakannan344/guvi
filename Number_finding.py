N,M=map(int,input().split())
A=list(map(int,input().split()[:N]))
B=list(map(int,input().split()[:M]))
C=[]
for i in range(N):
  for j in range(M):
    if (A[i]==B[j]):
      C.append(B[j])
B.sort()
C.sort()
if(B==C):
  print("YES")
else:
  print("NO")
