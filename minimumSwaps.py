"""
You are given an unordered array consisting of consecutive integers  
[1, 2, 3, ..., n] without any duplicates. You are allowed to swap 
any two elements. You need to find the minimum number of swaps 
required to sort the array in ascending order. 
"""

def minimumSwaps(arr):
    ref_arr = list(range(1,n+1))  
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0
    
    for i,v in enumerate(arr):
        correct_value = i+1
        if arr[i] != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
            #print(v,i)
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1
            

    print(swaps)

arr = [7,1,3,2,4,5,6]
n = len(arr)

minimumSwaps(arr)    