#importar la libreria nltk
import nltk 

# Definir la ruta donde se almacenarán los datos descargados de NLTK
nltk.data.path.append(r'C:/Users/elkin/AppData/Roaming/nltk_data')

# Descargamos la lista de palabras vacías stopwords que son palabras comunes como el, la, los, etc.
nltk.download('stopwords')

# Importar la función que divide un texto en palabras
from nltk.tokenize import word_tokenize

# Importar la lista de palabras vacías stopwords en español
from nltk.corpus import stopwords

# Imporar la herramienta para calcular la frecuencia de palabras en un texto
from nltk.probability import FreqDist

# Definimos un texto en español que queramos analizar

texto = """
Mi nombre es Laura Isabel Agudelo, tengo 33 años y soy Animadora Digital, diseñadora gráfica y de video, tengo una comunidad llamada Vuelve a conocer tu ciclo 
donde le enseño a las mujeres sobre alimentación cíclica, me gusta mucho leer y compartir el conocimiento que voy adquiriendo, disfruto pintar con acuarelas, y estoy aprendiendo a programar.

Mi compañero Wilmer es Ingeniero Industrial, con formación integral en análisis de procesos, gestión de proyectos, atención al cliente y mejora continua, enfocado en la optimización de sistemas organizacionales
bajo principios de eficiencia operativa y sostenibilidad. Cuenta con experiencia en sectores productivos y de servicios, donde ha liderado estrategias orientadas al control de inventarios, análisis de datos operativos, gestión de indicadores clave de rendimiento (KPI) y aplicación de metodologías Lean Six Sigma.

Mi compañero Anibal Baena, es Ingeniero de sistemas especialista en TIC´s; es un apasionado por la tecnología y la programación; tiene 51 años y está muy motivado conociendo como funciona la tokenizacion, entendiendo que es la base funcional del lenguaje natural para las máquinas.

Mi compañera Laura Yuliana Arias Ortiz, tiene 29 años, es auxiliar administrativa, pero Diseñadora Crossmedia de profesión
sus hobbies son, ir a cine, salir a pasear en su moto, bailar, hacer manualidades y salir a comer

Mi compañera Paola Aguirre, es tecnologa en análisis y desarrollo de sistemas, estudiante de ingeniería de sistemas, tiene 40 años, y sus hobbies son pasear y la tecnología.

"""

# Tokenización: Convertimos el texto en una lista de palabras individuales
palabras = word_tokenize(texto, language= 'spanish')

# Mostramos la lista de palabras obtenidas
print(palabras)

# Obtenemos la lista de palabras vacías en español, es decir, cargamos las stopwords en español. Aquí obtenemos una lista de palabras comunes en español que normalmente no necesistamos para el análisis. 
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras: eliminamos las stopwords y los signos de puntuación
# Recorremos cada palabra en una lista llamada palabras. Si la palabra no está en las stopwords y es una palabra real (sin números ni símbolos), la guardamos.

palabras_filtradas = [palabras for palabras in palabras if palabras.lower() not in stop_words and palabras.isalpha()]

# Mostramos la lista de palabras después del filtrado.
# Resultado: Nos quedamos solo con las palabras importantes.
print(palabras_filtradas)

# Calculamos la frecuencia de cada palabra en la lista filtrada
frecuencia_de_las_palabras = FreqDist(palabras_filtradas)

# Mostramos las 10 palabras más comunes y la cantidad de veces que aparecen
print(frecuencia_de_las_palabras.most_common(10))