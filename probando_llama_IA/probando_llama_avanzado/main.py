from clasificador import clasificar_mensaje_y_actualizar
from cofig_llama import groq_api_key
# Ejemplo de uso
if __name__ == "__main__":
    preguntas_abiertas = [
        "¿Cómo se hace el deploy en Railway?",
        "¿Qué diferencia hay entre RAG y fine-tuning?"
    ]

    mensaje_nuevo = "¿Se puede usar SQLite en producción con pocos usuarios?"
    clasificar_mensaje_y_actualizar(mensaje_nuevo, preguntas_abiertas)

    for pregunta in preguntas_abiertas:
        print(pregunta)
