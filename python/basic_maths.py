import math
''' reverse the no.'''
def reverse(n):
    q=0
    while n>0:
      
       p =n%10
       n = (n-p)/10
       q = q*10+p
    
    
    print("this is reverse",q)   
reverse(5676832)    

'''palindrom check'''

def is_palindrome(n):
    q=0
    l=n
    while n>0:
      
       p =n%10
       n = (n-p)/10
       q = q*10+p
    if l==q:
        print("this is palindrome")
    else:
        print("not palindrome")
        
is_palindrome(12361)

'''armstrong  check'''

def is_armstrong(n):
    sum =0
    temp = n
    while n>0:
        
        q = n%10
        n = (n-q)/10
        sum = sum + q*q*q
    if sum == temp:
         print("this is armstrong")
    else:
        print("not armstrong")
        
is_armstrong(2342)

''' all divisior'''

def all_divisior(n):
    factors = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if i!=n//i:
                factors.append(i)
                factors.append(n//i)
            else:
                factors.append(i)
            
    factors =sorted(factors)
    print(factors) 
    return factors
          
all_divisior(56)

''' gcd  of two numbers '''

def gcd(n,m):
    l =[]
    n_factors = all_divisior(n)
    m_factors = all_divisior(m)
    for i in n_factors:
        for j in m_factors:
            if i==j:
                l.append(i)
                
                
    print(f"{max(l)} is the gcd of {n}and{m}")           
    return max(l)

gcd(66,108)
             
             
''' short cut to gcd '''  

'''time complexity  is log(min(n,m)) '''
# gcd(n,m) = gcd(n%m,m)  till any one become zero
def gcd_shortcut(n,m):  
    while n>0 or m>0:
        if n>m:
           n = n%m
        else:
            m = m%n
    if n==0:
        return m
    else:
        return n
print(gcd(66,99))
    
    

