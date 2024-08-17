def swap(a,b):
    temp = a
    a =b
    b = temp
    return 




def reverse(l,r,a):
   if l>r:
       print(a)      # here print  prints only final result
       return a
   else:
                                 # here it prints for each transformation                                
                          
       a[l],a[r] = a[r],a[l]
       return reverse(l+1,r-1,a)
   
a=[3,4,6,7,4,9,8,1]


reverse(0,7,a)
      
      
''' reversing string'''     
      
      
def string_reverse(l,r,s):
   
    if l>r:
        
        s = ''.join(s)
        
        return s
    
    else:
        s=list(s)
        s[l],s[r]=s[r],s[l]
        
        
        return string_reverse(l+1,r-1,s)


s="hello ravi" 
print(string_reverse(0,9,s)) 



