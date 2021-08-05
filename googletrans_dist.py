from googletrans import Translator
import random
from languages import lang_codes

translator = Translator()
def distort(input_text: str, iterations=10) -> str:
    output = input_text 
    input_lang = translator.detect(input_text).lang

    for i in range(iterations):
        code, name = random.choice(list(lang_codes.items()))
        print(f"{i}: {name}")
        output = translator.translate(output, dest=code).text
    output = translator.translate(output, dest=input_lang).text
    return output

if __name__ == '__main__':
    input_text = str(input("Enter text to be distorted: "))
    distorted = distort(input_text, 10)
    print(distorted)