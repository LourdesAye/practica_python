# Crear cliente Chromadb
import chromadb
chroma_client = chromadb.Client()

# Crea una colección
# Las colecciones son donde almacenará sus incrustaciones (embeddings),
#  documentos y metadatos adicionales. 
# Las colecciones indexan sus incrustaciones y documentos, y permiten una recuperación y un filtrado eficientes. 
# Puede crear una colección con un nombre o devolverla si existe
collection = chroma_client.get_or_create_collection(name="my_collection")

# Agrega algunos documentos de texto a la colección
# Chroma almacenará tu texto y gestionará la incrustación e indexación automáticamente. 
# También puedes personalizar el modelo de incrustación. 
# Debes proporcionar identificadores de cadena únicos para tus documentos.

collection.upsert( # agregar elementos
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    ids=["id1", "id2"]
)

#Consultar la colección
# con una lista de textos de consulta y Chroma le devolverá el resultado.
results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)

#Si n_results no se proporciona, Chroma devolverá 10 resultados por defecto. 
# Aquí solo agregamos 2 documentos, así que configuramos n_resultados=2

