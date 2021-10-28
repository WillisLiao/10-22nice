n=int(input("0~255"))
b=int(input("2~9"))
a=0
c=1
d=0
e=0
while True:
    d+=n//b
    e+=n%b
    c+=1
    a+=10**c*(d)+10**(c-1)*(e)
    if d<b:
        break
print(a)





