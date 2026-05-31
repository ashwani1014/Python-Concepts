def print_num(n):
    if n>5:
        return
    
    print(n)
    return print_num(n+1)
    
print_num(1)    
    