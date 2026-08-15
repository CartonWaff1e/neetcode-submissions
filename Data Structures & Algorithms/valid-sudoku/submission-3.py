class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            filled = [ele for ele in row if ele != "."]
            if len(filled) != len(set(filled)):
                return False
        for col in range(9):
            filled = [board[row][col] for row in range(9) if board[row][col] != "."]
            if len(filled) != len(set(filled)):
                return False
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                filled = []
                for i in range(3):
                    for j in range(3):
                        if board[br + i][bc + j] != ".":
                            filled.append(board[br + i][bc + j])
                if len(filled) != len(set(filled)):
                    return False
        return True

        

            
            
                
            

