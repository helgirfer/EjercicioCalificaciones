'''
Created on 5 oct. 2021

@author: Usuario
'''
import unittest
from main.calificaciones import calcula_nota_cuestionario
from main.calificaciones import lee_datos_cuestionario

class calificaciones_test(unittest.TestCase):

    def test_calcula_nota_cuestionario(self):



        aciertos, errores, respuestas = lee_datos_cuestionario()   
        print("el numero de aciertos introducidos es " + str(aciertos))
        print("el numero de errores introducidos es " + str(errores))
        print("el numero de respuestas introducidos es " + str(respuestas))
        
        
        print("la nota final es " + str(calcula_nota_cuestionario( aciertos, errores, respuestas)))
               
        
if __name__ == "__main__":
    unittest.main()
