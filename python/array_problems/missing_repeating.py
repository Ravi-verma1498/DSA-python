
from typing import List
class sol:
    def mis_rep(self,a:List[int]):
        n = len(a)
        dict ={}
        for i in range(len(a)):
            if a[i] in dict :
                dict[a[i]]+=1
            else:
                dict[a[i]]=1
                
        s=1  
        r=0     
        for key in dict:
            # print(key)
            if dict[key]>1:
                r = key
                # print(key)
                
            if s in dict:  
                s+=1
                # print(s) 
                  
            if n not in dict:
                s = n
        print(s,r)
                
a= [3,1,2,6,4,6,7,5,8]           
sol = sol()
sol.mis_rep(a)