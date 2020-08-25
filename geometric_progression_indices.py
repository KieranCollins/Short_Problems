"""
You are given an array and you need to find number of tripets 
of indices (i,j,k) such that the elements at those indices are
in geometric progression for a given common ratio r and i<j<k. 
"""

import math

def countTriplets(arr, r):
    uniq = {}
    for i in range(n):
        key = arr[i]
        uniq[key] = uniq.get(key, 0) + 1
    count = 0
    if r == 1:
        for key in uniq:
            #nn= math.factorial(uniq[key]) # not needed k = 3
            kk = math.factorial(3)
            #nk = math.factorial(uniq[key]-3) # not needed k = 3
            count+= uniq[key]*(uniq[key]-1)*(uniq[key]-2)/kk
    elif r != 0:
        left = {}
        for i in range(n-1):
            one = arr[i]/r
            three = arr[i]*r
            if one in left != 0:
                if three in uniq != 0:
                    count += left[one]*uniq[three]
            uniq[arr[i]] -= 1
            left[arr[i]] = left.get(arr[i], 0) + 1
    print(int(count))



arr = [1,3,9,9,27,81]
r = 3 #ratio
n = len(arr)
countTriplets(arr, r)