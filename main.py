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
'''def initialize_mat(dim):
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
print(mat_mul(a,b))'''


#Comp-Intrs - for loop
def comp_int(pa, intrs, yrs):
  amount = 0
  for i in range(yrs):
    amount = pa * (1 + intrs / 100)
    pa = amount
  return amount

print(comp_int(100000, 30, 3))


#Comp-Intrs - recursion
def comp1(pa, intrs, n):
  
  amount = pa * (1 + intrs / 100)
  if (n == 1):
    return amount
  else:
    return comp1(amount, intrs, n - 1)
  '''
  comp1(pa, 30, 3)
  comp1(pa*1.3, 30, 2)
  comp1(pa*1.3*1.3, 30, 1)
  pa*1.3*1.3*1.3
  
  '''
print(comp1(100000, 30, 3))


def comp(p, n):
  if (n == 1):
    return p * (1.3)
  else:
    return comp(p, n - 1) * 1.3
    '''
    comp(p,3)
    comp(p,2)*1.3
    comp(p,1)*1.3*1.3
    p*1.3*1.3*1.3
    
    '''
print(comp(100000, 3))

def fact (n):
  if(n==1):
    return 1
  else:
    return n*fact(n-1)
'''
fact(5)
5*fact(4)
5*4*fact(3)
5*4*3*fact(2)
5*4*3*2*fact(1)
5*4*3*2*1



'''
print(fact(5))

def add(c,a=20,b=30): #default args
  return (a+b-c)
print(add(40,20,30)) #positional args
print(add(a=20,b=30,c=40)) #keyword agrs
print(add(40))
print(add(40,b=30))

def myFunction():
  global x
  x=x*2
  print('value x inside function',x)

x=5
print('value x before function',x)
myFunction()
print('value x after function',x)

