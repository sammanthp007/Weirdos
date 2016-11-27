class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer

    def coverPoints(self, X, Y):
        total_steps = 0
        for i in range(len(X) - 1):
            c_x = X[i]
            c_y = Y[i]
            f_x = X[i + 1]
            f_y = Y[i + 1]
            step = self.min_num_steps_to_reach(c_x, c_y, f_x, f_y)
            total_steps += step
        return total_steps

    def min_num_steps_to_reach(self, c_x, c_y, f_x, f_y):
        return max(abs(c_x - f_x), abs(c_y - f_y))

    def same_point(self, x, y, x1, y1):
        return (x == x1 and y == y1)

    def within_range(self, x, y, x1, y1):
        return abs(x - x1) < 2 and abs(y - y1) < 2

xs = [0, 3, 10]
ys = [0, 2, -28]
a = Solution()
s = a.coverPoints(xs, ys)
print(s)
