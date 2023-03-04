#Insertion Sort Algorithm
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while(j>=0 and A[j]>key):
            A[j+1] = A[j]
            j=j-1
        A[j+1] = key

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
insertionSort(A)
for x in A:
    print(x)