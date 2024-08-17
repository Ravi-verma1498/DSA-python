''' brute method ( finding all possible sub array then checking whose sum is k)'''

def brut(a,l):
    
    n = len(a)
    maxlen = 0
    for i in range(len(a)):
        for j in range(i,n):
            s=0
            for k in range(i,j+1):
                s +=a[k]
                
                if s == l:
                   
                    maxlen = max(maxlen,j-1-i)
    
    return maxlen


a = [2,3,5,1,2,3,1,1,1,1,1,9]
# k = 11   
# print(brut(a,k)          )
            
 
            
            
''' for positive  int only'''


    
            
# print(hashmethod(a,10))    
 
                
                
                

''' this is correct with my own modification'''

def posint(a,k):
    print(a)
    sum = 0
    maxlen=0
    dict={}
    for i in range(len(a)):
        sum = sum + a[i]
  
  
        dict[sum] = i+1
  
  
        rem = sum - k
        if rem ==0:
            maxlen = max(maxlen ,i+1)
            
        if rem in dict:
            length = i+1 -dict[rem]
            maxlen = max(maxlen,length)
            
    print(dict)    
            
    return maxlen
    
# print(posint(a,5))



''' for all integer '''
# def allint(a,k):
#     print(a)
#     sum = 0
#     maxlen=0
#     dict={}
    
#     for i in range(len(a)):
#         sum = sum + a[i]
#         if sum in dict:
#             dict[sum] +=1
#         else:
#            dict[sum] =1
         
#         rem = sum-k
#         # if rem in dict:
#             # length = 
#     print(min(dict[sum]))    
# a = [-1,3,1,1,2,-3,-2,4,-2]
# k = 1            
    
# allint(a,4)  


def tot_subarray_count(a,k) :
     n = len(a)
     dict = {}
     sum = 0
     count =0
     for i in range(n):
         sum +=a[i]
         dict[sum] = i
         if sum ==k:
             count +=1
         
         rem = sum - k
         if rem in dict :
             count +=1
             
     return count
 
 
# a = [3, 1, 2, 4]
print(tot_subarray(a,2))
             
        
    
         
         
         
         

            
    