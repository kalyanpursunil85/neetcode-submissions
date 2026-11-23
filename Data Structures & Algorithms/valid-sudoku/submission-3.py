from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R, C = len(board), len(board[0])
        r_map = defaultdict(set)
        c_map = defaultdict(set)
        s_map = defaultdict(set)
        for r in range(R):
            for c in range(C):
                if board[r][c] == ".":
                    continue
                if board[r][c] in r_map[r] or board[r][c] in c_map[c] or board[r][c] in s_map[(r//3, c//3)]:
                    return False
                else:
                    r_map[r].add(board[r][c])
                    c_map[c].add(board[r][c])
                    s_map[(r//3, c//3)].add(board[r][c])
        return True


