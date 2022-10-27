def add(a,b):
  ans=a+b
  return ans

print(add(3,7))

c =[[0,0,0],[0,0,0],[0,0,0]]
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
dim =len(a)
# c[i][j] =a[i][...]+b[...][j]
for i in range(dim):
  for j in range(dim):
    for k in range(dim):
      c[i][j]=c[i][j]+a[i][k]*b[k][j]

print(c)