import copy

# creación de clase Pregunta: para probar cómo afectan las copias a objetos mutables
class Pregunta:
    def __init__(self, texto, estado):
        self.texto = texto
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def __repr__(self):
        return f"Pregunta('{self.texto}', estado={self.estado})"


# creación de lista original con objetos de la clase Pregunta
original = [Pregunta("¿Qué es Python?", "pendiente"), 
            Pregunta("¿Cómo funcionan las listas?", "pendiente")]

# Creación de copia superficial con [:] 
copia = original[:]  # la lista es nueva, pero los elemntos mutables no se copian, se referencian (apuntan al mismo lugar en memoria)

# Modificamos el estado de una pregunta en la copia
copia[0].cambiar_estado("respondida") # se hacen cambios en el espacio de memoria que es referenciado por ambas preguntas

# La modificación del estado se ve reflejada en la original: porque el cambio es sobre el mismo espacio de memoria referenciado
print("Después de cambiar el estado en la copia:")
print("Original:", original)
print("Copia:", copia)

# Eliminamos un elemento de la copia
del copia[1] # se esta eliminando una referencia a un espacio de memoria, no el contenido de ese espacio

print("\nDespués de eliminar un elemento en la copia:")
print("Original:", original)  # La original sigue intacta (porque no se eliminó el contenido del espacio en memoria, se eliminó una referncia a ese espacio de memoria pero en la copia no en la original)
print("Copia:", copia)        # La copia ahora tiene un elemento menos

# Eliminamos un elemento de la original
del original[0]  #se esta eliminando una referencia a un espacio de memoria, no el contenido de ese espacio

print("\nDespués de eliminar un elemento en la original:")
print("Original:", original)  # Ahora solo tiene un elemento
print("Copia:", copia)        # La copia NO se ve afectada por esta eliminación

# Copia profunda con copy.deepcopy() para evitar compartir referencias
original_profunda = [Pregunta("¿Qué es Python?", "pendiente"), 
                     Pregunta("¿Cómo funcionan las listas?", "pendiente")]

copia_profunda = copy.deepcopy(original_profunda) # se crea un nuevo espacio de memoria para cada elemento sin compartir con la orginal

# Modificamos un atributo en la copia profunda
copia_profunda[0].cambiar_estado("respondida") # ya no se comparte el espacio en memoria

print("\nDespués de modificar el estado en la copia profunda:")
print("Original profunda:", original_profunda)  # No se ve afectada porque no se comparte espacio en memoria
print("Copia profunda:", copia_profunda)        # Solo la copia cambió

# Cuando usas copy.deepcopy(), se crea una nueva instancia para cada objeto dentro de la estructura de datos, 
# lo que significa que se asigna un nuevo espacio en memoria para cada elemento. 
# A diferencia de la copia superficial ([:]), que solo copia las referencias de los objetos mutables, 
# deepcopy() crea una replica completa e independiente.