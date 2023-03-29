from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='pt', target='en')

import json
file_in = open("dicionario_medico_aula.json", encoding='UTF-8')
dici = json.load(file_in)

new_dici = {}
for designation, description in dici.items():
    en_translation = translator.translate(designation)
    print(en_translation)
    new_dici[designation]= {
                            "des": description,
                            "en": en_translation
                            }
    
file_out = open("dicionario_translation.json")
json.dump(new_dici, ensure_ascii=False, indent=4)

file_out.close()

translator.translate("hoje está um dia bonito")

