from typing import List 
# from typing import Optional
class Solution:
    def print_spiral(self, m: List[List[int]]) -> None:
        n = len(m)
        top = 0
        bottom = n-1
        left =0
        right = n-1
        temp = []
        
        
        while(top<=bottom and left <=right):
            for i in range(left ,right+1):
                temp.append(m[top][i])
                # print(m[top][i],"h",i)
            top +=1
            
            for i in range(top,bottom+1):
                temp.append(m[i][right])
                # print(m[i][right],"o",i)
            right-=1
            
            for i in range(right,left-1,-1):
                temp.append(m[bottom][i])
                # print(m[bottom][i],"e",i)
            bottom -=1
            
            for j in range(bottom,top-1,-1):
                temp.append(m[j][left])
                # print(m[j][left],"l")
            left +=1
                
        print(temp)
        
mt = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

mt = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
sol = Solution()
sol.print_spiral(mt)
                
