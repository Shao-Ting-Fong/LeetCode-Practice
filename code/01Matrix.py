from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        n_row, n_col = len(mat), len(mat[0])
        q = []

        for r in range(n_row):
            for c in range(n_col):
                if mat[r][c] == 1:
                    mat[r][c] = -1
                else:
                    q.append((r, c))

        while q:
            nr, nc = q.pop(0)
            print((nr, nc))
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= nr + i < n_row and 0 <= nc + j < n_col and mat[nr + i][nc + j] == -1:
                    print('---', (nr + i, nc + j), '---')
                    mat[nr + i][nc + j] = mat[nr][nc] + 1
                    print(mat)
                    q.append((nr + i, nc + j))

        return mat
