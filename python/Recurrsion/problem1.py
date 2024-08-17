

# ''' Printing name n times using recursion'''
# def pri(i,n):
    
#     if i>n:
#         return 
    
#     else:
#         print("verma")
#         return pri(i+1,n)

# # pri(1,4)
   
   
    
# def prin(n,name):
#     if n==0:
#         return 
#     else:
#         print(name)
#         return prin(n-1,name)
# # prin(5,"Ravi")

# ''' printing 1 to n no. '''


# def num1(n):  # this print n to 1
#     if n<1:
#         return
#     else:
        
#         print(n)
#         return num1(n-1)
        
# # num1(10)

# '''# ***this is back tracking***   important'''

# def num2(n):  
#     if n<1:
#         return
#     else:
#         num2(n-1)  # this is crucial 
#         print(n)   # for more explanation check recursion 2 
        
        
# # num2(10)
    

# def num3(i,n): # this print  1 to n
#     if i>n:
#         return
#     else:
#         print(i)
#         return  num3(i+1,n)
# # num3(1,10)



# '''  find sum of 1 to n numbers'''
# def sum_num(n,s):
#     if n<1:
#         print(s)
#         return s
        
#     else:
#         return sum_num(n-1,s+n)
 
 
 
# #  ''' this method is more important'''   
# def sum_num2(n)  :
   
#     if (n<1):
       
#         return 0
#     else:
#         return n+sum_num2(n-1)
 
# print(sum_num2(5))




# '''  '''
# def fact(n):
#     if n==0 or n==1:
#         return 1
    
#     else :
#         return n*fact(n-1)
# print(fact(4))


''' fibonacci series'''
def fibo(n):
    if n==0 or n==1:
        return 1 
    else:
        
        return fibo(n-1) + fibo(n-2)
    
print(f"this is the fibo ser:{fibo(8)}")


    