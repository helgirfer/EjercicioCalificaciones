'''
Created on 5 oct. 2021

@author: Usuario
'''

def lee_datos_cuestionario():
    aciertos = input("introduce el numero de aciertos: ")
    errores = input("introduce el numero de errores: ")
    respuestas =input("introduce el numero de respuestas: ")
    
    return int(aciertos), int(errores), int(respuestas)

def calcula_nota_cuestionario(aciertos, errores, respuestas):
    nota = (aciertos * 10) /respuestas - (errores * 10) / (50 - respuestas)
    return max(0, nota) 