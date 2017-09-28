import re

rule1 = r'pen([cdjz])(.*)'

def stemmer(word, pattern):
    ganti = ''
    matched = re.match(rule1, word)
    if matched:
        return matched.group(1) + matched.group(2)
    return word

words = ['dimakan', 'dibuat', 'dirasakan', 'pendahulu', 'penjarah', 'penzazah', 'peniru']

for word in words:
    print(stemmer(word, rule1))