import re
#re = regex = regular expression
#ignorcase mengabaikan huruf kapital
#multiline mengabaikan enter/perpindahan baris

TEXT = """Kami               belajar tanpa lelah.
Kami& tidur tak teratur.
Kami kuliah dengan giat.
Kami korbankan masa#muda.
Itu karena kami ingin kelak istri dan anak kami bahagia.
ada     tikus"""

def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9 -]', ' ', text, flags = re.IGNORECASE|re.MULTILINE)# character sellain a-z, 0-9, " ", - digaanti dengan spasi kosong
    text = re.sub(r'( +)', ' ', text, flags = re.IGNORECASE|re.MULTILINE)# ( +) menandakan spasi berlebih akan diubah menjadi satu spasi saja
    tokens = text.split(" ") 
    return tokens

print(tokenize(TEXT))