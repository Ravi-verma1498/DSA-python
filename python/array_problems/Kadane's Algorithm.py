
''' similar to find longest sub array which
has the largest sum and returns its sum and prints the subarray ''' 
def kad(a):
    n = len(a)
    sum = -1110
    l = []
    dict = {}
    s=0
    e=0
    maxv=0
    for i in range(n):
        sum += a[i]
        # dict[sum]=i
        if sum >maxv:
            maxv = sum 
            s = 0
            e = i
        
        
        l.append(sum)
    # return maxv,dict,l
        
        for j in range(i):
            
            if l[i]-l[j]>SSmaxv:
                maxv = l[i]-l[j] 
                s= j
                e = i
    # print(a[s+1:e+1])
                
    print(maxv, a[s+1:e+1])  
    # print()     
    return maxv


arr = [-2,3,-1,4,-1,-3,-2,1,2,-1,4]  
# arr = [-1,3,-1,1,-4]  
# arr = [-2,1,-3,4,-1,2,1,-5,4] 
# print(arr[3:7])
# print(arr)        
kad(arr)
            