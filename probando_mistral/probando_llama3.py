# se usa para hacer peticiones HTTP a APIs (en este caso, a la API de Groq).
import requests 

# clave personal de API de Groq. Esto permite autenticarte para usar sus modelos de lenguaje.
GROQ_API_KEY = "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"

# recibe mensaje y devuelve su clasificación
def clasificar_mensaje(mensaje):
    # Dirección (URL) de la API de Groq para hacer completions estilo ChatGPT (generar texto a partir de un texto dado).
    url = "https://api.groq.com/openai/v1/chat/completions" # a dónde va el pedido
    # siempre que se envíe una petición a una API , va URL, cabecera y cuerpo
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}", # es iniciar sesión
        "Content-Type": "application/json" # me devuelve en formato json la respuesta
    }
    data = { # esto es un diccionario
        "model": "llama3-70b-8192", #Se especifica el modelo de lenguaje que se quiere usar
        "messages": [ # define el contexto de la conversación (como si fuera un ChatGPT).
            {
                "role": "system", # da instrucciones al modelo sobre cómo debe comportarse.
                "content": (
                    "Actuá como un experto en conversaciones de Discord educativas. "
                    "Tu tarea es clasificar si un mensaje del alumno es: "
                    "1) una pregunta nueva, "
                    "2) una repregunta relacionada a otra anterior, "
                    "3) una respuesta a otra persona. "
                    "Devolvé una sola palabra: 'pregunta', 'repregunta' o 'respuesta'."
                )
            },
            {"role": "user", "content": mensaje} # representa el mensaje que el usuario (en este caso, el alumno) escribió.
        ]
    }
    
    # El parámetro json=data le indica a requests que tome ese data (un diccionario de Python) 
    # y lo convierta a JSON antes de enviarlo. Se usa un diccionario aquí, pero la API lo recibe como JSON.
    # post: es para enviar datos para procesarlos
    response = requests.post(url, headers=headers, json=data) # Hace una petición HTTP POST a la API con la URL, cabeceras y datos definidos.
    
    print(response) # Eso es el objeto Response de la librería requests.
    # <Response [200]> : [200] significa “OK”, o sea, el servidor te respondió correctamente.
    # Pero eso no es el contenido real, sino solo el "envoltorio".

    # Siempre la API de Groq devuelve un JSON con esa estructura similar.
    #     {
    #   "id": "chatcmpl-abc123",
    #   "object": "chat.completion",
    #   "created": 1716650000,
    #   "model": "llama3-70b-8192",
    #   "choices": [
    #     {
    #       "index": 0,
    #       "message": {
    #         "role": "assistant",
    #         "content": "pregunta"
    #       },
    #       "finish_reason": "stop"
    #     }
    #   ],
    #   "usage": {
    #     "prompt_tokens": 123,
    #     "completion_tokens": 5,
    #     "total_tokens": 128
    #   }
    # }
    respuesta_json = response.json() # Convierte la respuesta en formato JSON a un diccionario de Python para poder procesarla.

    print(respuesta_json["usage"]["total_tokens"]) 
#     "usage": {
#     "prompt_tokens": X,
#     "completion_tokens": Y,
#     "total_tokens": X + Y
# }
# prompt_tokens: tokens que componen tu pregunta (entrada).
# completion_tokens: tokens que componen la respuesta del modelo.
# total_tokens: suma de ambos.

# 103 : Significa que entre tu prompt y la respuesta del modelo se usaron 103 tokens.

# ¿Por qué es útil esto?
# Si estás usando una API paga (como OpenAI), los tokens se cobran. Saber cuántos se usan ayuda a estimar costos.
# En modelos que tienen un límite (por ejemplo, 4k, 8k, 32k tokens), esto te dice cuánto estás ocupando.
# Para debugging: podés ver si un prompt muy largo está consumiendo muchos tokens.


    try:
        return respuesta_json["choices"][0]["message"]["content"].strip().lower()
        # ["choices"] : lista de respuestas del modelo.
        # [0] : primera respuesta.
        # "message": contenido del mensaje.
        # "content":  texto generado.
        # strip().lower() → elimina espacios al inicio/fin y lo pone en minúsculas.
    except KeyError:
        # Si hay un error (por ejemplo, no se encuentra la clave "choices"), se muestra el error y devuelve "error" como valor.
        print("Error:", respuesta_json)
        return "error"
    
# ¿Cómo sé que es un solo choice?
# Porque en el data no se pidio más de uno. Si quisieras más, tendrías que agregar:
# "n": 3  
# por ejemplo, para obtener 3 completions diferentes
# Entonces si no pone algo, por defecto te da uno solo (choices[0])

# Ejemplo de uso
mensaje = "¿Cómo configuro la conexión a PostgreSQL en Python?"
resultado = clasificar_mensaje(mensaje)
print("Clasificación:", resultado)