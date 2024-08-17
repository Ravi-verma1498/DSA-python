def coun(a):
    dict={}
    for i in range(len(a)):
        if a[i] in dict:
            dict[a[i]]+=1
        else:
            dict[a[i]]=1
        
    for i in dict:
        if dict[i]>len(a)/3:
            print(i)
a = [11,33,33,11,33,11 ]
# coun(a)


''' triplet sum Zero'''
from typing import List 
# from typing import Optional
class Sol:
    def zerotriplet(self, a: List[int]) -> None:
        n = len(a)
        a.sort()
        r = []
        
        for i in range(n):
            
            # if i>=1:
            if a[i] == a[i-1]:
                continue
            # else:
                
            for j in range(i+1,n):
                
                
                
                for p in range(n-1,j,-1):
                    
                    if  a[i]+a[j]+a[p]==0:
                        print("h")
                        
                        r.append([a[i],a[j],a[p]])
                        # to append multiple element at once in the array we use extend 
        print(r)  
        
        
        
        
    def merg_in_order(self,a1,a2):
        left = len(a1)-1
        right = 0
        
        # a1.sort()
        # a2.sort() 
    
        while left >=0 and right <=len(a2)-1  :
            print(left,right)
        
            if a1[left]>a2[right]:
                a1[left],a2[right]=a2[right],a1[left]
                left-=1
                right+=1
                print(a1+a2)
            else:
                break
                
        a1.sort()
        a2.sort()    
        print(a1+a2)
                
                     
                    

nums1 = [-1,0,1,2,-1,-4]
nums2=[-1,0,1,0]
arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
sol=Sol()

sol.merg_in_order(nums1,arr2)
     