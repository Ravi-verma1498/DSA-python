def mer(a):
    atemp=[]
    if len(a)>1:
        
        m = (len(a))//2
        
        l_arr = a[:m]
        r_arr = a[m:]
        
        mer(l_arr)
        mer(r_arr)
        
        i=0
        k=0
        j=0
            
        while(i<len(l_arr) and j<len(r_arr)):
            if a[i]<=a[j]:
                atemp[k] = a[i]
                i+=1
            else:
                atemp[k]=a[j]
                j+=1
            k+=1
        while (i<m):
            atemp[k] = a[i]
            i+=1
            k+=1
        while (j<len(r_arr)):
            atemp[k] = a[j]
            j+=1
            k+=1
        
      
        
    print(atemp)             
    
            
a = [9,8,7,5,6,4,3,1,2]
print(a)
print(mer(a))
            
        
        
        
        