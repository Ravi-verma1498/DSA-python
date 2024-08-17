def all_divisior(n):
    for i in range(1,int(math.sqrt(n))):
        if n%i==0:
            print(i,n//i)
            
all_divisior(36)