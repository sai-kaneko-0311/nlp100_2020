def word_bi_gram(str):
    results = {}
    strs = str.split()
    for i in range(len(strs)):
        if i == len(strs)-1:
            break
        pair = strs[i] + strs[i+1]
        if not pair in results.keys():
            results[pair] = 0
        results[pair] += 1
    return results

def char_bi_gram(str):
    results = {}
    for i in range(len(str)):
        if i == len(str)-1:
            break
        pair = str[i] + str[i+1]
        if not pair in results.keys():
            results[pair] = 0
        results[pair] += 1
    return results

str = "I am an NLPer"
print(word_bi_gram(str))
print(char_bi_gram(str))