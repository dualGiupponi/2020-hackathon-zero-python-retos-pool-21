from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    #Obtengo el elemento para hacer la comparación
    elemPlayer = options.index(player.lower().capitalize())
    elemAI = options.index(ai.lower().capitalize())
    resultado = ""

    #Caso de empate
    if elemAI == elemPlayer: resultado = "Empate!"
    #Casos que gana Player
    if elemPlayer == 0 and elemAI == 2: resultado = 'Ganaste!' #Piedra vs tijera
    if elemPlayer == 1 and elemAI == 0: resultado = 'Ganaste!' #Papel vs piedra
    if elemPlayer == 2 and elemAI == 1: resultado = 'Ganaste!' #Tijera vs papel
    
    #En caso de que no sea ninguno
    if resultado == "": resultado = 'Perdiste!'
    
    return resultado

# Entry Point
def Game():
    player = input()
    ai = input()
    
    winner = quienGana(player, ai)

    print(winner)
