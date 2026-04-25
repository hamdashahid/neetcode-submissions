class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = {}
        for i,r_val in enumerate(board):
            # check row duplicates
            temp = board[i]
            temp = [_ for _ in board[i] if _!="."]
            if len(set(temp)) != len(temp):
                return False
            # check column duplicates
            temp = [_[i] for _ in board if _[i]!="."]
            if len(set(temp)) != len(temp):
                return False
            # check squares
            for j,c_val in enumerate(board[i]):
                ind = (i//3)*3 +( j//3)
                squares[ind] = squares.get(ind,[])
                squares[ind].append(c_val)
        for k,val in squares.items():
            temp = [_ for _ in val if _!="."]
            if len(set(temp)) != len(temp):
                return False
        return True