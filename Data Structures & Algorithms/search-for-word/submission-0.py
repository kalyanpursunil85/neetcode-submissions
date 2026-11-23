class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def fn(i, x, y):
            if i == len(word) - 1:
                return board[x][y] == word[i]
            if board[x][y] != word[i]:
                return False
            temp = board[x][y]
            board[x][y] = "!"
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = dx + x, dy + y
                if 0 <= new_x < R and 0 <= new_y < C and board[new_x][new_y] != "!":
                    if fn(i+1, new_x, new_y):
                        return True
            board[x][y] = temp
            return False
        
        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and fn(0, i, j):
                    return True
        return False

