class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #use map of maps
        row = {}
        col = {}
        square = {}


            

        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j])
                if i not in row:
                    row[i] = set()
                if j not in col:
                    col[j] = set()
                if (i//3,j//3) not in square:
                    square[(i//3,j//3)] = set()
                
                if board[i][j] == ".":
                    pass

                elif board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in square[(i//3,j//3)]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    square[(i//3,j//3)].add(board[i][j])

        return True