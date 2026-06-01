import fitz

def extract_text(pdf_path):
    pdf = fitz.open(pdf_path)

    text = ""

    for page in pdf:
        text += page.get_text()

    return text

#8876892182:AAHvOW3SLOTH5OAB3-Zb35oxfwUVpJCXWWs