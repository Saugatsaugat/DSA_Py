#Bubble Sort Algorithm
#Issue in j block, when input is greater than 9, its loop starts through 1 instead of 0.
def bubbleSort(A):
    n = len(A)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(A[j]>A[j+1]):
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                #print(i,j)
                #print(A)

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
bubbleSort(A)
for x in A:
    print(x)
