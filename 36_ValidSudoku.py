class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxMaps = [dict() for x in range(9)]
        rowMaps = [dict() for x in range(9)]
        colMaps = [dict() for x in range(9)]
        
        valid = True
        
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                
                if(number != '.'):
                    if(rowMaps[i].get(number) == None):
                        rowMaps[i][number] = True
                    else:
                        valid = False

                    if(colMaps[j].get(number) == None):
                        colMaps[j][number] = True
                    else:
                        valid = False

                    boxNo = int(i/3)*3 + int(j/3)
                    boxPos = i%3*3 + j%3
                    if(boxMaps[boxNo].get(number) == None):
                        boxMaps[boxNo][number] = True
                        #print(boxNo, number)
                    else:
                        valid = False
                    
        return valid
                
