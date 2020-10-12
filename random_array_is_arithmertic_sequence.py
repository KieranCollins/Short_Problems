a = [-2, 2, -2]
b = [0, 0, 0]
c = [1, 5, 13]
d = [1,4,2,3]
e = [10, 10, 1, 1]

# Rerurn true if the array can be rearanged into an arithmetic sequence

# To reduce worst case time complexity count over for loop and recursion ending
# when the number of steps == len(arr)
# The worst case time complexity is O(n)
        
def check(arr):
    diff = (max(arr) - min(arr))/(len(arr)-1) 
    for i in range(len(arr)):
        arr = seq(diff,arr, i) # start recursion
        if arr == False:
            return()
            
    print(True)
    print(arr)  
    
def seq(diff,arr,i):
    if arr[i] != (min(arr)+i*diff): #check not sorted 
        if i == 0: # 0 edge case
            if min(arr) != 0: # edge case breaks
                print(False)
                print(arr) 
                return(False)
        check = (arr[i]-min(arr))% diff    
        if check != 0 or round(check) != check: # not in sequence breaks
                print(False)
                print(arr)
                return(False)
        j = int((arr[i]-min(arr))/ diff) #
        # index of  where the value should be
        if j < i:  #if passed break       
                print(False)
                print(arr) 
                return(False)
        arr[j],arr[i] = arr[i],arr[j]
        arr = seq(diff,arr, i)
    return(arr)        
    
        
check(a)
check(b)
check(c)
check(d)
check(e)
        
