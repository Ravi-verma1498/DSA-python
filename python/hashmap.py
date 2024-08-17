''' here dictionary is the hash map in python '''
hm = {}
hm["name"]="Ravi"
key = "team"
hm[key] = 'India'
# print(hm)


l=[]
l.append(hm.values())
# print(l)

# print(ord('h'))  ''' this is uni code'''


''' counting the frequency of char in strings similarly we can do for array'''


def freq(s):
    d ={}
    for char in s:
        if char in d:
            d[char]+=1
        else:
            d[char]=1
    return d

# print(freq("hello hellon"))

'''  finding char  or element with given freq'''
def find_arr(k,array):
    d = {}
    for i in array:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    b =[]
    b.append(d.values())
    print(max(b))
    p =[]
           
    for key in d:
        if d[key]==k:
           p.append(d.values())
           print(p)
    for key in d:
        if d[key]==max(b):
            print(key,d[key])
            
    return
    
    
a = [1,1,1,1,2,2,2,3,3,4]


print(find_arr(0,a)) 
    