class Solution:
        # @param A : tuple of integers
            # @param B : integer
                # @return an integer

    def diffPossible(self, A, B):
        if len(A) == 0:
            return 0

        set_of_needed = set()

        for i in A:
            if B == 0:
                if i in set_of_needed:
                    return 1

            set_of_needed.add(B + i)

        if B == 0:
            return 0

        for i in A:
            if i in set_of_needed:
                print (i)
                return 1
        return 0

a = Solution()
lis = [34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0,25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29]
b = 97
print(a.diffPossible(lis,b))
