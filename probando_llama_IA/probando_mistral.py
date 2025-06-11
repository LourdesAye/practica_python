import requests

# Asegurate de poner tu API Key real acá
API_KEY = "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"

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "Sos un asistente que clasifica mensajes de Discord como pregunta, repregunta o respuesta."},
        {"role": "user", "content": "¿Cuándo entregamos el práctico 3?"}
    ],
    "temperature": 0.2
}

response = requests.post(url, headers=headers, json=data)

# Ver toda la respuesta para debug
print(response.json())  

# Mostrar el contenido si todo va bien
if "choices" in response.json():
    print(response.json()["choices"][0]["message"]["content"])
else:
    print("Error: No se encontró la clave 'choices'")

#print(response.json()["choices"][0]["message"]["content"])