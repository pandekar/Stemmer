import re

TEXT = """Kami belajar tanpa lelah.
Kami& tidur tak teratur.
Kami kuliah dengan giat.
Kami korbankan masa#muda.
Itu karena kami ingin kelak istri dan anak kami bahagia."""

def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 -]', ' ', text, flags = re.IGNORECASE|re.MULTILINE)
    tokens = text.split(" ") 
    return tokens

print(tokenize(TEXT))