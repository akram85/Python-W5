'''def add(a,b):
  ans=a+b
  return ans

print(add(3,7))
'''
'''c =[[0,0,0],[0,0,0],[0,0,0]]
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
dim =len(a)
# c[i][j] =a[i][...]+b[...][j]
for i in range(dim):
  for j in range(dim):
    for k in range(dim):
      c[i][j]=c[i][j]+a[i][k]*b[k][j]

print(c)'''
# Matrix multiplication 
def initialize_mat(dim):
  C=[]
  for i in range(dim):
   C.append([])
  for j in range(dim):
    for k in range(dim):
      C[k].append(0)

  return C

def dot_product(u,v):
  dim =len(u)
  ans =0
  for i in range(dim):
    ans =ans +(u[i]*v[i])
  return ans

def row(M,i):
  dim =len(M)
  l=[]
  for k in range(dim):
    l.append(M[i][k])
  return l

def column(M,j):
  dim =len(M)
  l=[]
  for k in range(dim):
    l.append(M[k][j])
  return l

def mat_mul(A,B):
  dim =len(A)
  C= initialize_mat(dim)
  for i in range(dim):
    for j in range(dim):
      C[i][j] = dot_product(row(A,i),column(B,j))
  return C

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]
print(mat_mul(a,b))
  
  
  