import random
from textblob import TextBlob
from textblob import exceptions as textblobexceptions
from languages import lang_codes

def distort(input_text: str, iterations=10) -> str:
    blob = TextBlob(input_text)
    input_lang = blob.detect_language()
    output = input_text
    code, name = '', ''
    for i in range(1, iterations+1):
        blob = TextBlob(output)
        code, name = random.choice(list(lang_codes.items() - {code, name}))
        try:
            output = str(blob.translate(to=code).__str__()) # please never do this
        except textblobexceptions:
            pass
        print(f"{i}: {name} - {output[:20]}...")
    blob = TextBlob(output)
    output = blob.translate(to=input_lang)
    return output

if __name__ == '__main__':
    input_text = str(input("Enter text to be distorted: "))
    iterations = int(input("Enter the amount of iterations: "))
    distorted = distort(input_text, 50)
    print(distorted)
