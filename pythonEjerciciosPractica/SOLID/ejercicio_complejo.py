# #Desarrollar un chatbot en python que nos solicite algo y tome eso que le decimos, lo analice y nos responda cual es el sentimiento.

# Este proyecto busca aplicar varios aspectos, POO, módulos, API, analisis de datos, etc.
import openai


system_rol = '''Vas a simular ser un analizador de sentimientos. Voy a escribirte mensajes y quiero que lo analices y me des una respuesta con al menos 1 caracter y maximo 4 caracteres, solo respuestas numericas. donde -1 es negatividad maxima y 1 es positividad maxima. 0 es neutral. (Podes responder solo con int o float)'''

mensajes = [{"role": "system", "content": system_rol}]

class Analizador_de_sentimientos:
    def analizar_sentimiento(self, polaridad):
        if polaridad <= -0.6:
            return "\x1b[1;31m" + "Muy negativo"
        elif polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"
        elif polaridad < -0.1:
            return "\x1b[1;31m" + "Algo negativo"
        elif -0.1 <= polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral"
        elif polaridad < 0.4:
            return "\x1b[1;32m" + "Algo positivo"
        elif polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo"
        else:
            return "\x1b[1;32m" + "Muy positivo"


        
analizador = Analizador_de_sentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\n Decime algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 10
    )
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta})

    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)