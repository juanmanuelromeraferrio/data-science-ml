# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:44:50 2017

@author: Juan Manuel Romera, based on Joel Grus code from data-science-from-scratch 
"""

from probability import normal_approximation_to_binomial, normal_probability_below, normal_probability_between, normal_probability_above

if __name__ == "__main__":

    print()
    print("__Enfermos__")
    print()
    mu_0, sigma_0 = normal_approximation_to_binomial(100, 0.4)
    
    
    #probabildidad al menos 30 sobrevivan    
    a  = normal_probability_above(29.5, mu_0,sigma_0)
    print("Al menos 30 sobrevivan", a)
    
    #probabildidad mas de 46 sobrevivan    
    b  = normal_probability_above(46.5, mu_0,sigma_0)
    print("Mas de 46 sobrevivan", b)
    
    mu_1, sigma_1 = normal_approximation_to_binomial(100, 0.6)
    
    #probabildidad menos de 50 no sobrevivan 
    c  = normal_probability_below(49.5, mu_1,sigma_1)
    print("Menos de 50 no sobrevivan", c)
    
    
    print()
    print("__Examen__")
    print()
    
    #  Una prueba de opción múltiple tiene 200 preguntas, 
    #  cada una con  4 posibles respuestas, 
    #  de las cuáles solo una es la correcta 
    # ¿cuál es la probabilidad de que al azar 
    # se den de 25 a 30 respuestas correctas 
    # para 80 de las 200 preguntas  acerca de los cuales 
    # el estudiante no tiene conocimientos?
    
    
    #Binomial con n = 80 y p = 1/4
    
    mu_2, sigma_2 = normal_approximation_to_binomial(80, 0.25)
    d = normal_probability_between(24.5, 30.5, mu_2, sigma_2)
    
    print("Se den entre 25 y 30 respuestas correctas", d)
    
    print()
    print("__Productos Defectuosos__")
    print()
    
    #Si 35% de los productos manufacturados en cierta línea de producción es defectuoso, 
    #¿cuál es la probabilidad de que entre los siguientes 1000 productos 
    #manufacturados en esa línea 
     
    #c)exactamente 354 productos sean defectuosos?
    
    #Binomial n= 100 p=0.35
    mu_3, sigma_3 = normal_approximation_to_binomial(1000, 0.35)
    
    #menos de 354  productos sean defectuosos?,
    e  = normal_probability_below(353.5, mu_3,sigma_3)
    print("Menos de 354  productos sean defectuosos", e)
    
    #entre 342 y 364 productos sean defectuosos?
    f  = normal_probability_between(341.5,364.5, mu_3,sigma_3)
    print("Entre 342 y 364 productos sean defectuosos", f)
    
    #exactamente 354 productos sean defectuosos
    g  = normal_probability_between(353.5,354.5, mu_3,sigma_3)
    print("Exactamente 354 productos sean defectuosos", g)