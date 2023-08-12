def max(f,g,h):
    if f>g and f>h:
        return f
    elif g>f and g>h:
        return g
    else:
        return h
    

max_numb=max(2,3,3)
print('max is',  max_numb)