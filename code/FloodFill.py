from typing import List

class Solution:
    def floodFill1(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Recursive version:
        old_color = image[sr][sc]
        n_row, n_col = len(image), len(image[0])
        if color == old_color: return image

        def dfs(r, c):
            if image[r][c] == old_color:
                image[r][c] = color
                if r - 1 >= 0:    dfs(r - 1, c)
                if r + 1 < n_row: dfs(r + 1, c)
                if c - 1 >= 0:    dfs(r, c - 1)
                if c + 1 < n_col: dfs(r, c + 1)

        dfs(sr, sc)
        return image

    def floodFill2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # Code not using recursive
        old_color = image[sr][sc]
        n_row, n_col = len(image), len(image[0])
        pos = [(0,1), (0,-1), (-1,0), (1,0)]
        seen = set()
        stack = [(sr,sc)]

        while(stack):
            sr, sc = stack.pop()

            if (sr, sc) not in seen:
                seen.add((sr, sc))

                if image[sr][sc] == old_color:
                    image[sr][sc] = color

            for i,j in pos:
                if 0 <= sr + i < n_row and 0 <= sc + j < n_col:
                    if image[sr+i][sc+j] == old_color and (sr+i, sc+j) not in seen:
                        stack.append((sr+i, sc+j))
        return image


