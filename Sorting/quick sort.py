from random import randint

def qSort (A, nStart, nEnd):
    if nStart >= nEnd:
        return

    L = nStart
    R = nEnd
    X = A[(L + R) // 2]

    while L <= R:
        while A[L] < X:
            L += 1
        while A[R] > X:
            R -= 1
        if L <= R:
            A[L], A[R] = A[R], A[L]
            L += 1
            R -= 1
    qSort (A, nStart, R)
    qSort (A, L, nEnd)

N = 10
A = [randint(1,10) for i in range(N)]
print('Source array ', A)

qSort (A, 0, N-1)
print('Sorted array ', A)

qSort(A, 0, N-1)
