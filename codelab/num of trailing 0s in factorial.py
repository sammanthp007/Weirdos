class Solution:
        # @param A : integer
            # @return an integer

    def trailingZeroes(self, A):
        total = 0
        exp = 1
        while True:
            num_of_5 = A // (5 ** exp)

            if num_of_5 >= 1:
                total += int(num_of_5)
            else:
                break

            exp += 1
        return total
