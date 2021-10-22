n= int(input("0 ~ 255"))
a=0
for i in range(n-1):
    a+=1
    for i in range(a):
        if a%i==0:
            print(a)
    
