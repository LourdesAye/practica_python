import requests
from promps import obtener_prompt_analiza_mensaje
from cofig_llama import url,headers,armate_body
import time

MAX_INTENTOS = 3
# Función para llamar a LLaMA vía Groq (adaptala si ya tenés tu propio wrapper)
def llama_clasifica( mensaje, pregunta_abierta):
    body= armate_body(obtener_prompt_analiza_mensaje,pregunta_abierta,mensaje) # establecer url, headers y cuerpo
    # retry automático : si una operación (como un request a una API) falla, el sistema la intenta de nuevo automáticamente.
    # backoff : es el tiempo de espera antes de reintentar. Va aumentando con cada intento fallido, 
    # como una forma de "darle más aire" al servidor para que se recupere.
    # retry automático con backoff
    for i in range(MAX_INTENTOS):
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 429:
            espera = 2 ** i  # 1, 2, 4... segundos
            print(f"[WARN] Error 429 Too Many Requests. Esperando {espera}s y reintentando (intento {i+1})...")
            time.sleep(espera)
        else:
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip().upper()
    raise Exception("Demasiados intentos fallidos por 429.")


    # response = requests.post(url, headers=headers, json=body) # Hace una petición HTTP POST (procesar datos) a la API con la URL, cabeceras y datos definidos.
    # response.raise_for_status() 
    # es un método de la librería requests en Python que se usa para verificar si la solicitud HTTP fue exitosa. 
    # Si la respuesta del servidor tiene un código de estado que indica un error (cualquier código en el rango 4xx o 5xx), 
    # este método generará una excepción (requests.exceptions.HTTPError).
    # respuesta = response.json()["choices"][0]["message"]["content"].strip().upper()
    # response.json() : convierte la respuesta en formato JSON a un diccionario de Python para poder procesarla.
    # ["choices"] : lista de respuestas del modelo.
    # [0] : primera respuesta.
    # "message": contenido del mensaje.
    # "content" : texto generado.
    # strip().lower() → elimina espacios al inicio/fin y lo pone en minúsculas.
    # return respuesta

# Función principal
def clasificar_mensaje_y_actualizar(mensaje, preguntas_abiertas):
    resultados = []
    respuestas =[]

    for pregunta in preguntas_abiertas.copy():
        print(f"\n[INFO] Clasificando contra: {pregunta}")
        time.sleep(2)  # pausa de 2 segundo entre requests
        inicio = time.time()
        clasificacion = llama_clasifica(mensaje, pregunta)
        if clasificacion == "PREGUNTA":
            preguntas_abiertas.append(mensaje)
            #crear nueva pregunta.... 
        elif clasificacion == "RESPUESTA" or clasificacion ==  "REPREGUNTA":
            respuestas.append({
                "mensaje": mensaje,
                "tipo": clasificacion,
                "relacionada_a": pregunta
                })
        fin = time.time()
        print(f"[RESULTADO] Clasificación: {clasificacion} (tardó {fin - inicio:.2f} segundos)")
