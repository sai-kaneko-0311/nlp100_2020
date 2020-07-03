results = {}
for i, word in enumerate("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()):
    j = i + 1
    if j in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        results[word[0]] = j
    else:
        results[word[:2]] = j
print(results)