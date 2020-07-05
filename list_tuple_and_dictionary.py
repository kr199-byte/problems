#Assigning elements to different lists

list1=[1,"Rahul",56,1]

#add an extra element
list1.append("hello world")

#overwrite an existing element
list1[1]=23

#assign an element to certain index number.
list1.insert(2,100)
print(list1)



#Accessing element from tuple

tuple1=("tuple",4,83,"hello",90)
print(tuple1[2])
#Print all elements in a given tuple.
count=0
for element in tuple1:
    count+=1
    print(count,element)



#Deleting different dictionary elements.

di_1={'one':12,'two':89,'three':90,'four':100}
print("before deleting:",di_1)
del di_1['one']
print("after deleting:",di_1)
