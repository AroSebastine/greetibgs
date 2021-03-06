from page_functions import greetings
from translate import Translator

translator = Translator(to_lang='pt')


print(greetings.aro())


for greeting in greetings.Testing().greetings_list():
    print(translator.translate(greeting).title())
