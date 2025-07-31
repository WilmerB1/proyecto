# importar la libreria de nltk 
import nltk

#desde nltk descargar el paquete de stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

list_stopwords = stopwords.words('spanish')

# imprimir la lista de stopwords
print(list_stopwords)

