#trabalho de casa da aula 4
import json
import re

dicio_f = open("dic_medico_pequeno.json", encoding='UTF-8')

dicio = json.load(dicio_f)

#livro_f = open('LIVRO-Doenças-do-Aparelho-Digestivo.txt') porque este é muito grande
livro_f = open('livrinho.txt', encoding='UTF-8')

result_f=open("result.html", "w", encoding='UTF-8')

text = livro_f.read()


blacklist=['e', 'de', 'são'] 

nova_lista = [re.escape(designacao) for designacao in dicio.keys() if designacao not in blacklist]

#nova_lista = dicio.keys() - blacklist

expressao = r"\b(" + "|".join(nova_lista) + r")\b"

body = '<body>'

def anotaTermo(termo):
    termo = termo[1]
    return "<a data-toggle='tooltip' href='' title='" + dicio[termo] + "'>"+termo+" </a>"

text = re.sub(expressao, anotaTermo, text)
text = re.sub(r"\f", "<hr>", text)
text = re.sub(r"\n", "<br>", text)


body += text


body += "</body>"        

result_f.write(body)

livro_f.close()
dicio_f.close()