Leetcode Problem: 118

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        def _generate(i, j):
            if j == 0 or i == j:
                return 1
            # The following line of code will be executed when code is coming back from-
            # line number 13 to find previously generated nums, for adding together. 
            elif i < len(result) and j < len(result[i]):
                return result[i][j]
            
            return _generate(i-1, j-1) + _generate(i-1, j)
        
        for i in range(numRows):
            row = []
            for j in range(0, i+1):
                row.append(_generate(i, j))
            result.append(row)
        return result
