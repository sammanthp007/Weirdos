"""Rewrite the MERGE procedure so that it does not use sentinels, 
instead stopping once either array L or R has had all its elements copied 
back to A and then copying the remainder of the other array back into A.
"""

def merge(A, p, q, r):
    L = A[p:q]
    H = A[q:r + 1]
    l = p
    h = q
    k = p
    while (l < len(L) and h < len(H)):
        if L[l] <= H[h]:
            A[k] = L[l]
            l += 1
        else:
            A[k] = H[h]
            h += 1
        k += 1
    while (l < len(L)):
        A[k] = L[l]
        k += 1
        l += 1
    while (h < len(H)):
        A[k] = H[h]
        k += 1
        h += 1

def mergesort(A, p, q):
    print("samman")
    print(q)
    if p < q:
        mid = (p + q) // 2
        mergesort(A, p, mid)
        mergesort(A, mid, q)
        merge(A, p, mid, q)


arr = [3,21,4]
mergesort(arr, 0, len(arr) - 1)
print(arr)
