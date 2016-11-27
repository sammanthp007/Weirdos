class Solution:
        # @param A : integer
            # @return an integer

    def reverse(self, A):
        if A < 0:
            neg = 1
        else:
            neg = 0

        A = abs(A)

        new_num = 0
        while A:
            new_num = new_num * 10 + A % 10
            A = A / 10

            if neg:
                new_num = 0 - new_num

            if new_num > 2**31 or new_num < -2**31:
                return 0

        return new_num
