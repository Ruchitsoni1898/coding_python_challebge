def lower_indexes(word):
    l=[]
    for i,v in enumerate(word):
        if v.islower():
         l.append(i)
    return l

print(lower_indexes("HAllo"))


