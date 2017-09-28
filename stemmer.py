import re

def stemmer(word):
    pattern = r'di'
    ganti = ''
    word = re.sub(pattern, ganti, word)
    return word

words = ['dimakan', 'dibuat', 'dirasakan']

for word in words:
    print(stemmer(word))