# Transformar o ficheiro txt em html

import re
file = open ('dicionario_medico.txt', encoding='utf8')
text = file.read()

# remover os ff
text = re.sub(r'\f', '', text)

entries = re.findall(r'\n\n(.+)((?:\n.+)+)', text)

#rmeover os \n 
new_entries = [(designation, description.strip()) for designation, description in entries]


'''for designation, description in entries:
    description = description.strip()
    new_entries.append((designation, description))
'''

print(new_entries[10])

file.close()

html = open ('dicionario_medico.html', 'w',encoding='utf8' )

header = '''<html>
<head> 
<meta charset='utf-8'/>
</head>
<body>
'''

body = ''
for designation, description in new_entries:
    body += ' <tr><td>' + designation + '</b>'
    body += '<p>' + description + ' ' + ' '

footer = ''' </body>
</html>'''

html.write(header + body + footer)


html.close()