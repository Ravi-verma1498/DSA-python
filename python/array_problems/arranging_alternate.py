''' 
There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
Without altering the relative order of positive and negative elements, you must return an
array of alternately positive and negative values.  


Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5

Explanation: 

Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.'''

def alt(a):
    n = len(a)
    odd = 1
    even = 0
    temp =[0]*n  # we need define the non-empty array of fixed length as "con't fill higher index without filling lower index" 
    for i in range(len(a)):
        if a[i]>0 and even < len(a):
            print('h')
            temp[even] = a[i]
            even +=2
        else:
            print('o')
            temp[odd] = a[i]
            odd +=2
    return temp
arr = [1,2,-3,-1,-2,3]
print(alt(arr))