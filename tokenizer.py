TEXT = """Kami belajar tanpa lelah."""

def tokenize(text):
    text = text.lower()
    tokens = text.split(" ")
    return tokens

print(tokenize(TEXT))