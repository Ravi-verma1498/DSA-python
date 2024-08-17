from typing import List 
# from typing import Optional
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
    # def mat(m):
        n=len(matrix)

        temp =  [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                    temp[i][j]=matrix[n-1-j][i] 
                    
                    
        print(temp)
        return temp

m = [[1,2,3],[4,5,6],[7,8,9]]
mt = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

sol = Solution()
sol.rotate(mt)




                 
    