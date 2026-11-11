class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        seen_p = set()
        seen_a = set()

        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]

        def dfs(r, c, seen):
            if (r, c) in seen:
                return

            seen.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        # Pacific: górna i lewa krawędź
        for c in range(cols):
            dfs(0, c, seen_p)

        for r in range(rows):
            dfs(r, 0, seen_p)

        # Atlantic: dolna i prawa krawędź
        for c in range(cols):
            dfs(rows - 1, c, seen_a)

        for r in range(rows):
            dfs(r, cols - 1, seen_a)

        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if (r, c) in seen_p and (r, c) in seen_a
        ]
