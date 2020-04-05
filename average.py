n=[]
a=0
b=0
for i in range(1,11):
    n.append(int(input()))
for j in range(0,10):
    a=a+n[j]
b=a/10
print(b)
