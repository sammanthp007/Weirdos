class Solution:
        # @param A : list of integers
            # @param B : integer
                # @return an integer

    def removeElement(self, A, B):
        l = len(A) - 1
        c = 0
        while c != l:
            if A[c] == B:
                A[c], A[l] = A[l], A[c]
                l -= 1
            else:
                c += 1
        A = A[:c]
        print(A)
        return c


    def removeElementAns(self, A, B):
        n = len(A)
        k = 0
        for i in range(n):
            if A[i] == B:
                k += 1
            elif k > 0:
                A[i - k] = A[i]
        A = A[:n - k]
        print(A)
        return n - k


a = Solution()
lis = [2, 3, 4, 3, 4, 5, 2, 5, 7, 4, 63, 4, 2, 3, 5, 6, 3]
b = 3
print(a.removeElement(lis, b))
print(a.removeElementAns(lis, b))
