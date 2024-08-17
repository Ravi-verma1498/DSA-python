'''  important concept '''
# how travers a array without too much loop using pointer 

def sort(a):
     n= len(a)
     low =0
     mid = 0
     high = n-1
     while mid<=high:
         
         if a[mid] == 0:
             a[mid],a[low]= a[low],a[mid]
             low = low+1
             mid = mid+1
         elif a[mid]==1:
             mid=mid+1
             
         else:
            a[mid],a[high]=a[high],a[mid]
            high=high-1
     return a
            
arr = [0, 2, 1, 2, 0, 1,0,1]   
       
print(sort(arr) )
             
             
             