class Solution:
        # @param A : integer
            # @return a boolean

    def isPower(self, N):
        if N == 0:
            return False
        if N == 1:
            return True
        for p in range(2, 33):
            coef = int(N**(1.0 / p))
            for i in range(2, coef + 2):
                if i**p == N:
                    print(coef, p)
                    return True
        return False

num = 823543
print(num ** (1.0 / 7))
a = Solution()
print(a.isPower(823543))
