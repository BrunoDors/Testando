def dobralencol(lençol, gaveta):
    if (lençol < gaveta):
        return 0 
    else:
        return 1 + dobralencol(lençol /2 , gaveta)
    
print(dobralencol(200,25))

