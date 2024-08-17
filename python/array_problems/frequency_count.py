def freq(a):
    n = len(a)

    dict = {}
    maxf=0
    for i in range(n):
       
        if a[i] in dict:
            
            dict[a[i] ] +=1
            maxf = max(maxf,dict[a[i]])
        else:
        
            dict[a[i]] = 1
            
    print(dict)
    keys = [key for key ,value in dict.items() if value == maxf]
    return keys

    
arr = [2,2,1,1,1,2,2] 
print(freq(arr))
        
