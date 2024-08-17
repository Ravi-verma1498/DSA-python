import numpy as np

# 
# def selection_sort(array):
#     for i in range(len(array)):
#         if min(array) ==array[i]:
#             array[i], array[0] = array[0], array[i]
#             array.pop(0)
#             return selection_sort(array)
        
a = [9,5,8,4,7,2,3,1,]
# print(selection_sort(a))



# def sel(a):
#     print(a)  
#     for i in range(len(a)-1):
#         for j in range(i,len(a)):
#             if  a[j] == min(a[i:]):             
#                 a[i],a[j] = a[j],a[i]
#     print("selection sort",a)
#     return a
        
# sel(a)
''' buble sort'''
    
# def bub(a):
#     n = len(a)
#     for i in range(len(a)):
       
#         for j in range (1,len(a)-i):
            
#             if a[j-1] >= a[j]:
#                a[j-1],a[j] = a[j],a[j-1]
#     print("buble sort",a)          
#     return a

# bub(a)


''' insetion sort'''
def iner(a):
    n = len(a)
    
    for i in range(n):
      
        for j in range(i,0,-1):    # for backward loop  important to mention the steps
            if a[j]<=a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
           
        print(a)
    return a

iner(a)
            
            
                
                
            
            