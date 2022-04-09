class CSP:
    def __init__(self,board) -> None:
        ROW = "ABCDEFGHI"
        COL = "123456789"   
        self.variables = list(ROW[r] + COL[c] 
                        for r in range(9) for c in range(9))
        self.domain = self._generateDomain(board)
        self.scope = self._generateScope()
        self.neighbors = self._generateNeighbors()
        self.constraints = {(var, nb) for var in self.variables for nb in self.neighbors[var]}
        self.pruned = {}
    
    def _generateDomain(self, board):
        domain = {}
        for cell in self.variables:
            domain[cell] = str(board[cell])
            if board[cell]==0:
                domain[cell]='123456789'
        return domain

    def _generateScope(self):
        ROW = "ABCDEFGHI"
        COL = "123456789"
        row_scope = []
        col_scope = []
        square_scope = []

        for i in range(9):
            row = []
            col = []
            for j in range(9):
                row.append(ROW[i]+COL[j])
                col.append(ROW[j]+COL[i])

            row_scope.append(row)
            col_scope.append(col)
            
        for i in range(0,9,3):
            ALPHA = ROW[i:i+3]
            for j in range(0,9,3):
                NUMB = COL[j:j+3] 
                
                JJ = []
                for a in ALPHA:
                    for b in NUMB:
                        JJ.append(a+b)
                        
                square_scope.append(JJ)

        return col_scope+row_scope+square_scope

    def _generateNeighbors(self):
        n = dict()
        for var in self.variables:
            n[var]=[]
            for scope in self.scope:
                if var in scope:
                    for item in scope:
                        if item!=var:
                            n[var].append(item)
            n[var]=set(n[var])
        return n
