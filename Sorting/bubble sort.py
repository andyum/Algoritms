from random import randint

N = 10
A = [randint(1,10) for i in range(N)]
print("Source array ", A)

for i in range(N-1):
    for j in range(N-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

print("Sorted array ", A)
