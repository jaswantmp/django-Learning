# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:19:47 2026

@author: Jaswant MP
"""


def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True


def armstr(n):
    d=len(str(n))
    print(d)
    a=0
    for i in str(n):
        a+=(int(i)**d)
    if a==n:
        print("Armstrong number")
    else:
        print("not an Armstrong number")
        
        
def squnum(n):
    l=[]
    for i in range(2*n-1):
        a=[]
        for j in range(2*n-1):
            left=i
            top=j
            right=(2*n-2)-i
            bottom=(2*n-2)-j
            m=n-min(left,top,right,bottom)
            a.append(m)
        l.append(a)
    for i in l:
        for j in i:
            print(j,end=' ')
        print()
        
        
def butpattern(n):
    s=2*n-2
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        for j in range(s):
            print('  ',end='')
        s-=2
        for j in range(i+1):
            print('*',end=' ')
        print()
    s=2
    for i in range(n-1):
        for j in range(n-i-1):
            print('*',end=' ')
        for j in range(s):
            print('  ',end='')
        s+=2
        for j in range(n-i-1):
            print('*',end=' ')
        print()
        
        
def optmerge():
    c=0
    l=[5,10,20,30]
    while(len(l)>1):
        a=min(l)
        l.remove(a)
        b=min(l)
        l.remove(b)
        c+=(a+b)
        l.append(a+b)
    print(c)
        
'''
n=int(input("number: "))
if prime(n):
    print("prime")
else:
    print("Not prime")
armstr(n)
squnum(n)
butpattern(n)
optmerge()
'''
# knapsack

'''

maxv=0
def ks(n,w,v,t,ind,iv):
    global maxv
    if t<0:
        return
    if maxv < iv :
        maxv=iv
    if ind==n:
        return
    ks(n,w,v,t-w[ind],ind+1,iv+v[ind])
    ks(n,w,v,t,ind+1,iv)
    
    
n=4
w=[1,3,4,5]
v=[1,4,5,7]
t=7
ks(n,w,v,t,0,0)
print(maxv)
'''

# betting result

'''
import random
import matplotlib.pyplot as plt
a=0
x=[]
y=[]
for i in range(365*5):
    x.append(i+1)
    bet=random.randint(1,10)
    ld=random.randint(1,10)
    if bet==ld:
        a+=900-100
    else:
        a-=100
    y.append(a)
print("Amount : ",a)
plt.plot(x,y)
plt.show()
'''

# X/O game

'''
import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def cr(s):
    for r in range(3):
        cnt=0
        for c in range(3):
            if board[r][c]==s:
                cnt+=1
        if cnt==3:
            return True

def cc(s):
    for c in range(3):
        cnt=0
        for r in range(3):
            if board[r][c]==s:
                cnt+=1
        if cnt==3:
            return True
        
def cd(s):
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==s:
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]==s:
        return True
    return False

def won(s):
    return cr(s) or cc(s) or cd(s)

def place(s):
    print(numpy.matrix(board))
    while(1):
        row=int(input("\nEnter Row: 1 or 2 or 3: "))
        col=int(input("\nEnter col: 1 or 2 or 3: "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("Invalid tryagain")
    board[row-1][col-1]=s

def play():
    for i in range(9):
        if i%2==0:
            print("\n X turn \n")
            place(p1s)
            if won(p1s):
                print(p1s, " Won !!!")
                break
        else:
            print("\n O turn \n")
            place(p2s)
            if won(p2s):
                print(p2s, " Won !!!")
                break
    if not(won(p1s)) and not(won(p2s)):
        print("Draw")
play()'''



#Magic Square

def magicsquare(n):
     if n%2==0:
        print("n always be odd so change n value as an odd number\n")
        return
    
     ms=[]
     for i in range(n):
         l=[]
         for j in range(n):
             l.append(0)
         ms.append(l)
     i=n//2
     j=n-1
     num=n*n
     count=1
     while(count<=num):
         if(i==-1 and j==n):
             j=n-2   
             i=0
         else:
             if(j==n):
                 j=0
             if(i<0):
                 i=n-1 
         if(ms[i][j]!=0):
             j=j-2
             i=i+1
             continue
         else:
            ms[i][j]=count
            count+=1
         i=i-1
         j=j+1
     for i in range(n):
        for j in range (n):
            print(ms[i][j],end=" ")
        print()
     print("The sum of each row/column/diagonal is: ",n*(n**2+1)/2)
     
magicsquare(11)