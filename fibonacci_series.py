#fibonacci series using python

a=0
b=1
count=100
list_f=[]
for i in range(count):
    list_f.append(a)
    c=a+b
    a=b
    b=c
print(list_f)
