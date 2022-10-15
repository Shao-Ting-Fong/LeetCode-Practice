from typing import List

class Solution:
    def solution1(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(N*M)
        # Space Complexity: O(1)

        # Solution 1: Recursion
        n_row, n_col = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if 0 <= r < n_row and 0 <= c < n_col and grid[r][c]:
                grid[r][c] = 0  # 讓看過的格子變成0，節省重複計算的時間
                return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return 0

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea

    def solution2(self, grid: List[List[int]]) -> int:
        # Solution 2: Non-recursive

        pos = [(0,1), (0,-1), (-1,0), (1,0)]
        seen = set()

        for sr, row in enumerate(grid):
            for sc, value in enumerate(row):

                if value and (sr, sc) not in seen:
                    area = 0
                    stack = [(sr, sc)]

                    while stack:

                        r, c = stack.pop()

                        if (r, c) not in seen and grid[r][c]:
                            seen.add((r, c))
                            area += 1

                        for i,j in pos:
                            if 0 <= r+i < n_row and 0 <= c+j < n_col:
                                if grid[r+i][c+j] and (r+i, c+j) not in seen:
                                    stack.append((r+i, c+j))

                    maxArea = max(area, maxArea)

        return maxArea







