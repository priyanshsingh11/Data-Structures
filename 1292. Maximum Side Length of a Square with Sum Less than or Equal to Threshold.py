class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        ans = 0
        for i in range(m):
            for j in range(n):

                size = ans + 1

                while i + size <= m and j + size <= n:
                    square_sum = (
                        prefix[i + size][j + size]
                        - prefix[i][j + size]
                        - prefix[i + size][j]
                        + prefix[i][j]
                    )

                    if square_sum <= threshold:
                        ans = size
                        size += 1
                    else:
                        break

        return ans
