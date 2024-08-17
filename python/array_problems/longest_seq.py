def lon(a):
   
    st =set(a)
    longest=0
    for i in range(len(a)):    
        s =a[i]+1
        
        c=1
        # while s in a     ## it has time complexity o(n) for checking element in array
        while s in st:     ## it has time complexity o(1) for checking element in set
            
            s = s+1
            c+=1
        longest = max(c,longest)
    return longest

a = [100,5, 200, 101,102,103, 104,99,97]
print(lon(a))