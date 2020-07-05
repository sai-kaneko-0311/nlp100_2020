import random


def order_rand(str):
    results = []
    for word in str.split():
        word_be_joined = word
        if not len(word) <= 4:
            target_shuffle = [
                char for char in word_be_joined[1:len(word_be_joined)-1:1]]
            random.shuffle(target_shuffle)
            word_be_joined = word[0] + ''.join(target_shuffle) + word[-1]
        results.append(word_be_joined)
    return ' '.join(results)


str = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print(order_rand(str))
