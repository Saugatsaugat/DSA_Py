#Merge Sort Algorithm
import math
def mergeSort(A,l,r):
    if(l<r):
        m = math.floor((l+r)/2)
        mergeSort(A,l,m)
        mergeSort(A,m+1,r)
        merge(A,l,m,r)

def merge(A,l,m,r):
    x = l
    y = m+1
    k = 1
    B = []
    while(x<=m and y<=r):
        if(A[x]<A[y]):
            B.append(A[x])
            x=x+1
            k=k+1
        else:
            B.append(A[y])
            y = y+1
            k = k+1
    while(x<=m):
        B.append(A[x])
        x = x+1
        k = k+1
    while(y<=r):
        B.append(A[y])
        y = y+1
        k = k+1
    for i in range(l,r):
        A[i] = B[i]

getSize = int(input("How many elements you want to sort? "))
print(f"Enter {getSize} elements\n")
A = []
for x in range(0,getSize):
    a = int(input())
    A.append(a)
print("Before Sort\n")
for x in A:
    print(x)
print("After Sort\n")
l = int(A[0])
r = int(A[getSize-1])
mergeSort(A,l,r)
for x in A:
    print(x)

