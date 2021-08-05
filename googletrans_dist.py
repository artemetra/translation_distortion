from googletrans import Translator
import random
from languages import lang_codes

input_text = str(input())
output = ""
iterations = 10

translator = Translator()
input_lang = translator.detect(input_text).lang
output = input_text 

for i in range(iterations):
    name, code = random.choice(list(lang_codes.items()))
    print(str(name))
    output = translator.translate(output, dest=code).text
    # print(str(output))
output = translator.translate(output, dest=input_lang).text
print(output)