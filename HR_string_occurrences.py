#Checking if by removing 1 character maximum
#All characters have the same number of 
#occurrences in a string
from collections import Counter


s = "aabbccddee"

def isValid(s):
    my_count = Counter(s).values()
    final_count = Counter(my_count).values()  
    if len(final_count) > 2:
        return("NO")
    count = False
    for i in final_count:
        if i >1:
            if count == True:
                return("NO") 
            count = True
    return("YES")    


print(isValid(s))    
