a= int(input())
b= int(input())
if(a>b):
    num=b
else:
    num=a
for i in range(1, num+1):
    if(a%i==0 and b%i==0):
        gcd=i
print(gcd)        
