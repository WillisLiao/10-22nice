n= int(input())
f=0
if n==1:
    f+=(n+1)
while n!=1:
    f+=(n+1)
    n//2
    n=n-1
    
f+=(n+1)





print(f)
    