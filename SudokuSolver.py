class SudokuSolver:
    def __init__(self, gameBoard_in):
        self.gameBoard = gameBoard_in

    def run(self):
        row = 0
        col = 0
        forward = True
        while row != 9 and row != -1:
            if not self.gameBoard[row][col][0]:
                self.gameBoard[row][col][1] += 1
                num = self.gameBoard[row][col][1]
                if num != 10:
                    if self.checkRow(row) and self.checkCol(col) and self.checkSquare(row, col):
                        row, col = self.addCol(row, col)
                        forward = True
                else:
                    self.gameBoard[row][col][1] = 0
                    row, col = self.minusCol(row, col)
                    forward = False
            else:
                if forward:
                    row, col = self.addCol(row, col)
                else:
                    row, col = self.minusCol(row, col)
        if row == -1:
            print("This sudoku puzzle in unsolvable")
        else:
            print("Solved Board: ")
            for i in range(9):
                for j in range(9):
                    print(self.gameBoard[i][j][1], end = " ")
                print()
            return self.gameBoard

    def addCol(self, row, col):
        col += 1
        if col == 9:
            row += 1
            col = 0
        return row, col

    def minusCol(self, row, col):
        col -= 1
        if col == -1:
            row -= 1
            col = 8
        return row, col

    def checkRow(self, row):
        rowStorage = set()
        for element in self.gameBoard[row]:
            if (not element[1] in rowStorage) and (element[1] != 0):
                rowStorage.add(element[1])
            elif element[1] != 0:
                return False
        return True

    def checkCol(self, col):
        colStorage = set()
        for element in self.gameBoard:
            if (not element[col][1] in colStorage) and (element[col][1] != 0):
                colStorage.add(element[col][1])
            elif element[col][1] != 0:
                return False
        return True

    def checkSquare(self, row, col):
        squareStorage = set()
        startRow = int(row / 3) * 3
        startCol = int(col / 3) * 3
        for i in range(3):
            for j in range(3):
                num = self.gameBoard[startRow + i][startCol + j][1]
                if (not num in squareStorage) and (num != 0):
                    squareStorage.add(num)
                elif num != 0:
                    return False
        return True
