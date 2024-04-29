# Importación de las bibliotecas necesarias
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# Texto de ejemplo
texto = """Alicia empezaba ya a cansarse de estar sentada con
su hermana a la orilla del río, sin tener nada que
hacer: había echado un par de ojeadas al libro que su
hermana estaba leyendo, pero no tenía dibujos ni
diálogos. «¿Y de qué sirve un libro sin dibujos ni diá-
logos?», se preguntaba Alicia.
Así pues, estaba pensando (y pensar le costaba
cierto esfuerzo, porque el calor del día la había dejado
soñolienta y atontada) si el placer de tejer una guir-
nalda de margaritas la compensaría del trabajo de le-
vantarse y coger las mar-
garitas, cuando de pronto
saltó cerca de ella un Cone-
jo Blanco de ojos rosados.
No había nada muy ex-
traordinario en esto, ni
tampoco le pareció a Alicia
muy extraño oír que el co-
nejo se decía a sí mismo:
«¡Dios mío! ¡Dios mío! ¡Voy
a llegar tarde!» (Cuando
pensó en ello después, de-
cidió que, desde luego, hu-
biera debido sorprenderla mucho, pero en aquel mo-
mento le pareció lo más natural del mundo). Pero
cuando el conejo se sacó un reloj de bolsillo del cha-
leco, lo miró y echó a correr, Alicia se levantó de un
salto, porque comprendió de golpe que ella nunca
había visto un conejo con chaleco, ni con reloj que
sacarse de él, y, ardiendo de curiosidad, se puso a
correr tras el conejo por la pradera, y llegó justo a
tiempo para ver cómo se precipitaba en una madri-
guera que se abría al pie del seto.
Un momento más tarde, Alicia se metía también
en la madriguera, sin pararse a considerar cómo se
las arreglaría después para salir.
Al principio, la madriguera del conejo se extendía
en línea recta como un túnel, y después torció brus-
camente hacia abajo, tan bruscamente que Alicia no
tuvo siquiera tiempo de pensar en detenerse y se en-
contró cayendo por lo que parecía un pozo muy pro-
fundo.
O el pozo era en verdad profundo, o ella caía muy
despacio, porque Alicia, mientras descendía, tuvo
tiempo sobrado para mirar a su alrededor y para
preguntarse qué iba a suceder después. Primero, in-
tentó mirar hacia abajo y ver a dónde iría a parar,
pero estaba todo demasiado oscuro para distinguir
nada. Después miró hacia las paredes del pozo y ob-
servó que estaban cubiertas de armarios y estantes
para libros: aquí y allá vio mapas y cuadros, colgados
de clavos. Cogió, a su paso, un jarro de los estantes.
Llevaba una etiqueta que decía: MERMELADA DE NA-
RANJA, pero vio, con desencanto, que estaba vacío.
No le pareció bien tirarlo al fondo, por miedo a
matar a alguien que anduviera por abajo, y se las
arregló para dejarlo en otro de los estantes mientras
seguía descendiendo.
«¡Vaya!», pensó Alicia. «¡Después de una caída
como ésta, rodar por las escaleras me parecerá algo
sin importancia! ¡Qué valiente me encontrarán todos!
¡Ni siquiera lloraría, aunque me cayera del tejado!» (Y
era verdad.) Abajo, abajo, abajo. ¿No acabaría nunca
de caer?
—Me gustaría saber cuántas millas he descendido
ya —dijo en voz alta—. Tengo que estar bastante cer-
ca del centro de la tierra. Veamos: creo que está a
cuatro mil millas de profundidad...
Como veis, Alicia había aprendido algunas cosas
de éstas en las clases de la escuela, y aunque no era
un momento muy oportuno para presumir de sus co-
nocimientos, ya que no había nadie allí que pudiera
escucharla, le pareció que repetirlo le servía de repaso.
"""
# Creación del objeto WordCloud
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate(texto)
# Visualización del WordCloud generado
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()