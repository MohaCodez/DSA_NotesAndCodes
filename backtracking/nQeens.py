def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        nDiag = set()
        pDiag = set()

        res = []
        board = [["."]*n for i in range(n)] #initialize the board

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in pDiag or (r-c) in nDiag:
                    continue
            
                col.add(c)
                pDiag.add(r+c)
                nDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pDiag.remove(r+c)
                nDiag.remove(r-c)
                board[r][c]= "."

        backtrack(0)
        return res
