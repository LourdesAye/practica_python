from langchain.embeddings import HuggingFaceEmbeddings # para cargar modelo que genera embeddings
from langchain.vectorstores import Chroma # para crear base de datos vectorial en ChromaDB


# Carga un modelo preentrenado que transforma texto en vectores
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Preguntas simuladas desde Discord
preguntas = [
    "¿Cuál es la diferencia entre TCP y UDP?",
    "¿Cómo se crea una clase en Python?",
    "¿Qué es una base de datos relacional?",
    "¿Cómo uso Git en un proyecto?",
]

# Metadatos opcionales (útiles para guardar autor, timestamp, etc.)
metadatos = [{"id": str(i+1)} for i in range(len(preguntas))]

#Crear base de datos vectorial en ChromaDB
# Transforma cada pregunta en un vector, lo guarda en ChromaDB, y permite hacer búsquedas por similitud semántic
# Guardamos los vectores localmente en "./chroma"
vectordb = Chroma.from_texts(
    texts=preguntas,
    embedding=embedding_model,
    metadatas=metadatos,
    persist_directory="./chroma"
)
vectordb.persist()  # guarda los datos en disco

# Convierte la pregunta nueva en vector, 
# lo compara con los guardados y devuelve los más parecidos. 
# Sirve para saber si ya se respondió algo similar.
# Nueva pregunta del alumno (simulada)
pregunta_nueva = "¿Para qué sirve UDP en redes?"

# Buscamos las 2 preguntas más similares
resultados = vectordb.similarity_search(query=pregunta_nueva, k=2)

# Mostramos los resultados
for r in resultados:
    print("Texto similar:", r.page_content)
    print("Metadatos:", r.metadata)


#Cómo cargar un modelo de embeddings en LangChain.
#Cómo transformar preguntas en vectores.
#Cómo almacenar y persistir vectores con ChromaDB.
#Cómo hacer una búsqueda semántica.

