def char_bigram(str):
    results = {}
    for i in range(len(str)):
        if i == len(str)-1:
            break
        pair = str[i] + str[i+1]
        if not pair in results.keys():
            results[pair] = 0
        results[pair] += 1
    return results


str_x = "paraparaparadise"
str_y = "paragraph"

X = char_bigram(str_x)
Y = char_bigram(str_y)
print(X)
print(Y)
print(f'union: {X.keys() | Y.keys()}')
print(f'intersection: {X.keys() & Y.keys()}')
print(f'diff(X-Y): {X.keys() - Y.keys()}')
print(f'diff(Y-X): {Y.keys() - X.keys()}')
print(f'se in X: {"se" in X.keys()}')
print(f'se in Y: {"se" in Y.keys()}')
