def shift(n): 

    lis=[10,20,30,40,50,60] 
    lis1=[]

    for i in range(n,len(lis)): 
        lis1.append(lis[i])
    for i in range(0,n):
        lis1.append(lis[i])    
        
    print(lis1)
         
shift(3)    