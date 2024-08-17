
'''   here we use just pattern  method to get pascle traingle only things     '''


def pascle(n):
    for i in range(1,1+n):
        ans = 1
        
        for j in range(n,i,-1):
            print("",end="   ")
        
        for j in range(i):
            
            print(ans,end ="     ")
            
            ans = int(ans*(i-j-1)/(j+1))
            
        print('\n')  
       
pascle(10)