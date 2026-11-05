class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj

                if (
                    0 <= ni < len(grid)
                    and 0 <= nj < len(grid[0])
                    and grid[ni][nj] == "1"
                    and (ni, nj) not in seen
                ):
                    seen.add((ni, nj))
                    dfs(ni, nj)

        seen = set()
        land = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    land += 1
                    seen.add((i, j))
                    dfs(i, j)

        return land