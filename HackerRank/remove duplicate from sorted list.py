class Solution:
        # @param A : list of integers
            # @return an integer

    def removeDuplicates(self, A):
        i = 0
        while i < len(A):
            curr = A[i]
            j = i + 1
            while (j < len(A) and curr == A[j]):
                A.pop(j)
                i += 1
        return len(A)
    
    def more_Effecient_remove_duplicates(self, A):
        i = 0
        j = 0
        n = len(A)
        while (i < n and j < n):
            if j + 1 >= n:
                return i + 1

            if A[j] == A[j + 1]:
                j += 1
            else:
                A[i + 1] = A[j + 1]
                j += 1
                i += 1
