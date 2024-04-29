from textblob import TextBlob

# Crear un objeto TextBlob
texto = TextBlob("TextBlob es una herramienta increíble para procesamiento de lenguaje natural.")

# Análisis de sentimientos
analisis_sentimientos = texto.sentiment

print("Polaridad:", analisis_sentimientos.polarity)
print("Subjetividad:", analisis_sentimientos.subjectivity)