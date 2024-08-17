n =6
p = 6

'''# Pyramid shape'''
# for i in range(n):
#     for j in range(n-i):
#         print( " ",end="")          
        
#     for k in range(i):
#         print("*",end=" ") 
        
#     for l in range(n-i):
#         print(" ",end="")
        
#     print("\n")   # print('\n')
   
''' # Dimond shape'''

# for i in range(n):
#     for j in range(n-i):
#         print( " ",end="  ")          
        
#     for k in range(i):
#         print(" *  ",end="  ") 
        
#     for l in range(n-i):
#         print( " ",end="   ")
        
#     print("\n") 
# for i in range(n):
#     for j in range(i):
#         print( " ",end="  ")          
        
#     for k in range(n-i):
#         print(" *  ",end="  ") 
        
#     for l in range(i):
#         print( " ",end="   ")
        
#     print("\n") 
    
'''  # side pyramid'''
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print("\n")
''' number(0,1) pyramid '''
# for i in range(n):
#     for j in range(i):
#         if j%2==0:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print('\n')

''' number horn pattern'''
# for i in range(n):
#     for j in range(i):
#         print(j+1,end=" ")
#     for j in range(n-1-i):
#         print(" ",end="   ")
#     for j in range(i): 
#         print(i-j,end =" ")   
#     print("\n")
''' tricky number pattern '''
# for i in range(n):
#     for j in range(i):      # can also use n = 1 and then n+=1
#         # print(i,end="")    #print(n)
#         if i<=2:  
#             print(i+j,end=" ")
#         elif i==3:
#             print(i+j+1,end=" ")
#         else:
#             print(i+j+2,end=" ")
#     print("\n")

''' pattern with alphabet'''
# for i in range(n):
#     str = 'ABCDEFGHIJK'
#     for j in range(i):
#         print(str[j],end=" ")
#     print('\n')
    
    
''' inverted alphabet  pattern'''
# for i in range(n):
#     str = 'ABCDEFGHIJK'
#     for j in range(n-i):
#         print(str[j],end=" ")
#     print('\n')
    
    
''' '''   
# for i in range(n):
#     str = 'ABCDEFGHIJK'
#     for j in range(i):
#         print(str[i-1],end=" ")
#     print("\n")
    
''' **** imp concept alpha pattern  '''
n=4
# for i in range(n):
#     str='ABCDEFGHIJ'
#     for j in range(n-i):
#         print(" " ,end=" ")
#     for j in range(i//2):
        
#         print(str[j],end="   ")
#     for j in range(i//2,i):
#         print(str[abs(i-j-1)],end ="   ")
#     for j in range(n-i):
#         print(" " ,end=" ")
#     print("\n")


'''  tricky alpha'''
# n = 6
# for i in range(1,n):
#     str ='xABCDEFGHIJKlMN'
#     for j in range(i):
#         print(str[n-i+j],end=" ")
#     print("\n")

 
''' '''
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(i):
#         print("",end="    ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print("\n")  
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(n-i):
#         print("",end="    ")
#     for j in range(i):
#         print("*",end=" ")
#     print("\n")
''' Square Shape ''' 
# for i in range(n) :
#     for j in range(n):
#         if i==0:
#             print("*",end="    ")
#         elif i==n-1:
#             print("*",end="    ")
#         else:
#             if j==0 or j==n-1:
#                print("*",end="  ")
#             else :
#                 print(" ",end ="     ")
#     print("\n")
'''  very important  check out striver pattern's
last pattern to get sol  here this is incorrect code'''
for i in range(n):
    for j in range(i):
        print(n-j,end="    ")  
    # for j in range(i):
    #     print(" ",end=" ")   
    for j in range(n-i):
        print(n-i,end= "    ")
    
    for j in range(i):
        print(n-i+j+1,end="   ")  
        
    print("\n")