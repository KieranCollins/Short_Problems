#Returns the single super digit for an integer (n) consecrated (k) times 
#Too much code duplication here

def super(n):
    if len(str(n)) == 1:
        return(n)
    else:
        
        string = str(n)
        count = 0
        for i in string:
           
            count += int(i)
            print(string)
        result = super(count)
        return(result)

def superDigit(n, k):
    if len(str(n)) == 1:
        return(n)
    string = str(n)
    count = 0
    for i in string:
        count += int(i)
    result = super(count*k)
    return(result)

n= 123
k=3

result = superDigit(n, k)

print(result)
