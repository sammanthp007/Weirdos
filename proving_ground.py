class Solution:
        # @param A : integer
            # @return a boolean

    def isPower(self, N):
        if N == 0:
            return False
        if N == 1:
            return True
        for p in range(2, 33):
            for A in range(2, int(N**(1.0 / p)) + 2):
                if A**p == N:
                    print(A, p)
                    return True
        return False


a = Solution()
print(a.isPower(823543))
