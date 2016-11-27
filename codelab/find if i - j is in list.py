class Solution:
        # @param A : list of integers
            # @param B : integer
                # @return an integer

    def diffPossible(self, A, B):
        if len(A) == 0:
            return 0

        for i in range(len(A)):
            s = A[i]
            j = i + 1
            while j < len(A):
                l = A[j]
                if l - s == B:
                    return 1
                if l - s > B:
                    break
                j += 1
        return 0


a = Solution()
lis = [2,3,4,5,6,7,8,9]
b = 5
print(a.diffPossible(lis,b))
