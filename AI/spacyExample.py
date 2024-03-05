import spacy

# Cargar el modelo de lenguaje español
nlp = spacy.load('es_core_news_sm')

# Texto de ejemplo en español
texto = """Por cuanto por parte de vos, Miguel de Cervantes, nos fue fecha relación
que habíades compuesto un libro intitulado El ingenioso hidalgo de la
Mancha, el cual os había costado mucho trabajo y era muy útil y provechoso,
nos pedistes y suplicastes os mandásemos dar licencia y facultad para le
poder imprimir, y previlegio por el tiempo que fuésemos servidos, o como la
nuestra merced fuese; lo cual visto por los del nuestro Consejo, por cuanto
en el dicho libro se hicieron las diligencias que la premática últimamente
por nos fecha sobre la impresión de los libros dispone, fue acordado que
debíamos mandar dar esta nuestra cédula para vos, en la dicha razón; y nos
tuvímoslo por bien. Por la cual, por os hacer bien y merced, os damos
licencia y facultad para que vos, o la persona que vuestro poder hubiere, y
no otra alguna, podáis imprimir el dicho libro, intitulado El ingenioso
hidalgo de la Mancha, que desuso se hace mención, en todos estos nuestros
reinos de Castilla, por tiempo y espacio de diez años, que corran y se
cuenten desde el dicho día de la data desta nuestra cédula; so pena que la
persona o personas que, sin tener vuestro poder, lo imprimiere o vendiere,
o hiciere imprimir o vender, por el mesmo caso pierda la impresión que
hiciere, con los moldes y aparejos della; y más, incurra en pena de
cincuenta mil maravedís cada vez que lo contrario hiciere."
"""

# Procesar el texto
doc = nlp(texto)

# Tokenización y eliminación de stopwords, y lematización (aproximación a stemming)
tokens_limpios = [token.lemma_ for token in doc if not token.is_stop]

print(tokens_limpios)