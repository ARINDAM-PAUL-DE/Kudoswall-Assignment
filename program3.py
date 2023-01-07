def rotateArray(x:list, t:int):
    for i in range(0,t):
        element=x[i]
        x.append(element)
    
    x = x[t:]
    return x

x = [1,2,3,4,5,6]

print(rotateArray(x, 2))
    