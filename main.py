#Importamos librerias que usaremos en la trivia
import time
import random
#Creamos las variables que se asignarán a los coloes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[39m"

#Puntaje inicial
puntaje = 0
# Iniciamos la variable en True
iniciar_trivia = True
#Variable que guardará el número de intentos de la trivia
intentos = 0
print("**Bienvenido a mi trivia sobre Contabilidad.**")
time.sleep(1)
print("Pondremos a prueba tus conocimientos.")
puntaje = 0
print("Tienes", puntaje, "puntos.")
name = input("Ingresa tu nombre: ")

print(
    "Hola", name,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando Enter para enviar. SUERTE!"
)
time.sleep(1)
puntaje = 0
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
while iniciar_trivia == True:
  intentos+= 1
  puntaje = 0
  print("Intento número: ", intentos)
  input("Presiona Enter para continuar.")
  print("Empezamos en: ")
  for i in range(5,0,-1):
    print(i)
    time.sleep(1)
  print(
    "Hola", name,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando Enter para enviar. SUERTE!"
)
  time.sleep(1)

  print("1) ¿Cuánto es el valor del IGV para las empresas del Régimen general?")
  time.sleep(1)
  print("a) 16%")
  print("b) 17%")
  print("c) 18%")
  print("d) 10%")
  respuesta1 = input("Ingresa tu respuesta: ")
  while respuesta1 not in ("a", "b", "c", "d"):
        respuesta1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta1 == "a":
        puntaje += +5
        print("Muy bien", name, "!")
    
  else:
        puntaje += -3
        print("Incorrecto", name, "!")
        print(puntaje)
    
  print(name, "llevas", puntaje, "puntos")
  time.sleep(1)
    
    #Pregunta2
  print(
        "\n2) ¿Cuánto es lo que puede pagar por impuesto a la renta mensual en el Régimen RUS?"
    )
  time.sleep(1)
  print("a) 30 o 50 soles")
  print("b) 30 o 60 soles")
  print("c) 20 o 50 soles")
  print("d) 20 o 60 soles")
  respuesta2 = input("Ingresa tu respuesta: ")
    
  while respuesta2 not in ("a", "b", "c", "d"):
        respuesta2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta2 == "c":
        puntaje += 5
        print("Muy bien", name, "!")
  else:
        puntaje += -2
        print("Incorrecto", name, "!")
    
  print(name, "llevas", puntaje, "puntos")
  time.sleep(1)
  print(
        "\n1) ¿Cuál de las siguientes alternativas no es un Régimen Tributario en el Perú?"
    )
  time.sleep(1)
  print("a) Régimen General")
  print("b) Régimen MYPE Tributario")
  print("c) Régimen Especial a la Renta")
  print("d) Régimen de Perción del IGV")
  respuesta3 = input("Ingresa tu respuesta: ")
  while respuesta3 not in ("a", "b", "c", "d"):
        respuesta3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta3 == "a":
        puntaje += -2
        print("Incorrecto!", name,
              "Régimen General es un Régimen tributario del Perú")
  elif respuesta3 == "b":
        puntaje += -2
        print("Incorrecto!", name,
              "Régimen MYPE Tributario es un Régimen tributario del Perú")
  elif respuesta3 == "c":
        puntaje += -2
        print("Incorrecto!", name,
              "Régimen Especial a la Renta es un Régimen tributario del Perú")
  else:
        puntaje += 5
        print("Muy bien", name, "!")
  print(name, "llevas", puntaje, "puntos")
  time.sleep(1)
  print("\n1) ¿Qué significa UIT")
  time.sleep(1)
  print("a) Unidad Interna Tributaria")
  print("b) Unidad de Impuesto a la Trivia")
  print("c) Unidad Impositiva Tributaria")
  print("d) Unidad Implícita al Tesoro")
  respuesta3 = input("Ingresa tu respuesta: ")
  while respuesta3 not in ("a", "b", "c", "d"):
        respuesta3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    
  if respuesta3 == "a":
        puntaje += -2
        print("Incorrecto!", name, "Unidad Interna Tributaria no existe")
  elif respuesta3 == "b":
        puntaje += -2
        print("Incorrecto!", name, "Unidad de Impuesto a la Trivia no existe")
  elif respuesta3 == "d":
        puntaje += -2
        print("Incorrecto!", name, "Unidad Implícita al Tesoro no existe")
  else:
        puntaje += 5
        print("Muy bien", name, "!")
  print("Gracias", name, "por jugar mi trivia, lograste ", puntaje, " puntos")
    #Preguntar si quiere volver a jugar la trivia
  print("¿Deseas intentar nuevamente la trivia?")
  repetir_trivia = input(
        "Ingresa 'si' para repetirlo o cualquier tecla para finalizar:").lower()
    #Función lógica
if puntaje >= 13:
  print(GREEN+"A continuación, para que puedas subir tu puntaje te aparecerá ALEATORIAMENTE tendras que ingresas 3 número del 1 al 4."+RESET)
  number1=input("Ingresa el primer número: ")
  number2=input("Ingresa el segundo número: ")
  number3=input("Ingresa el tercer número: ")
else 
  print(CYAN+"Gracias,",name,",por jugar mi trivia, lograste alcanzar", puntaje," puntos."+RESET)

 if repetir_trivia != "si":
     print(BLUE+"\nEspero que lo hayas pasado bien,",nombre,".Hasta pronto!"+RESET)
     iniciar_trivia = False