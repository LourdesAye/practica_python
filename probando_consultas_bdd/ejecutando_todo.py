# crear vectores
from crear_vectores import crear_base_vectorial
vectordb = crear_base_vectorial()

# probar búsqueda semántica
from utilidades_vectores import probar_busqueda
probar_busqueda(vectordb, "¿Qué es Github?", k=5)
probar_busqueda(vectordb, "¿Cómo se usa el patrón state?", k=5)
probar_busqueda(vectordb, "¿qué es java?",k=5)

# Eliminar base vectorial
#from utilidades_vectores import eliminar_vectores_chroma
#eliminar_vectores_chroma()
