#Finding the number of matching pairs 

n = 9
ar = [10,20,20,10,10,30,50,10,20]

def matchingpairs(n, ar):
    counts = 0
    counted =  [0] * n 
    for i in range(n): 
        for j in range(i,n): 
            if i ==j:
                pass
            elif counted[i] or counted[j] != 0:
                pass
            elif ar[i] == ar[j]:
                counted[i],counted[j] = 1,1
                counts += 1
    print(counts)

matchingpairs(n, ar)    
