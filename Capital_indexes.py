def capital_indexes(word):
    l = []
    for i, v in enumerate(word):
        if v.isupper():
            l.append(i)
    return l  # Ensure this is outside the for loop

# Example usage:
print(capital_indexes("RUCHIT"))

