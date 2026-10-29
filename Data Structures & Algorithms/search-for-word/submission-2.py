class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(pos: tuple, target: int) -> bool:
            y, x = pos

            if target == len(word):
                return True

            visited.add(pos)

            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + dy, x + dx

                if (
                    0 <= ny < len(board)
                    and 0 <= nx < len(board[0])
                    and (ny, nx) not in visited
                    and board[ny][nx] == word[target]
                ):
                    if dfs((ny, nx), target + 1):
                        return True

            visited.remove(pos)
            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    if dfs((y, x), 1):
                        return True

        return False