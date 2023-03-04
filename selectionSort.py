#Selection Sort Algorithms
def selectionSort(A):
    n = len(A)
    for i in range(0,n):
        least = A[i]
        p = i
        for j in range(i+1,n):
            if(A[j]<least):
                least = A[j]
                p = j
        temp = A[i]
        A[i] = A[p]
        A[p] = temp

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
selectionSort(A)
for x in A:
    print(x)

