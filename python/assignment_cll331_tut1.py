import random
import os
import matplotlib.pyplot


def disp(n,t):
    s = [0]*n
    directory = "D:\c++\dsa\python"
    x=[]
    y=[]
    for i in range(t):
        
        for j in range(n):
    
            p = random.uniform(0,1)
            if p>=0.5 :
                s[j] = s[j]+1
            else :
                s[j]=s[j]-1  
        avg_x= sum([x**2 for x in s])/n
        print(i,    avg_x)
        x.append(i)
        y.append(avg_x)
        # output_filename = os.path.join(directory,"output.txt")
        # with open(output_filename, "w") as output_file:
        #     output_file.write( f"x= {i}  ,  y = {sum([x**2 for x in s])/n}")
 
    return sum([x**2 for x in s])

 
disp(6,10)            
    
            
