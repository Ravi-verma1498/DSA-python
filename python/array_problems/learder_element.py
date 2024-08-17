def leader_element(a):
    print(a)
    k = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
              
                k = 1
            else: 
                
                k = 0
                break
        if k == 1:
            print(a[i])
    return 


arr = [4, 7, 1, 0]
arr =  [10, 22, 12, 3, 0, 6]
leader_element(arr)
    
    
        
                
                