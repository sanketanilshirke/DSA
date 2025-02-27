# Given an array with some integer type values. Write a python script to sort array values?
from array import *
A = array ('i', [23, 54, 22, 1, 2, 12])
print(sorted(A))
print(type(A))


# Given a list of heterogeneous elements. Write a py script to remove all the non int values from the list.
list2 = ['Vinay',24,54,224,65,'rupesh','yuvi']
num=[]
for k in list2:
    if isinstance(k,int):
        num.append(k)
print(num)


# Write a Python script to calculate average of elements of a list.
list = [23,55,32,56,99,64,23,34]
average = sum(list) / len(list)
print (average)


# Write a Python script to create a list of first N prime numbers.
n = int(input("Enter the number is:"))
l3=[]
for i in range(2,n+1):
    count=0
    for j in range(2,i):
        if (i%j)==0:
            count=+1
    if count == 0:
        l3.append(i)
print(l3)


# write py script to create a list of first n terms of fibbonacci series.
fibonacci = int(input("Enter Number:"))
a=0
b=1
result=[a,b]
for i in range(2,fibonacci):
    result.append(result[-1] + result[-2])
print(result)




