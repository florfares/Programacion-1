# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 15:35:57 2025

@author: ffares
"""


import os
os.getcwd()
os.chdir('C:/Users/fares/OneDrive - Universidad Nacional de San Martin/LCD/Programación I/ejercicios_python/Parcial1')
#%%
## Ejercicio 1
def leer_ventas(nombre_archivo):
    import csv
    libros = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        
        try:
            for row in rows:
                lote = {'titulo':row[0], 'genero': row[1], 'precio': float(row[2]), 'cantidad':int(row[3])}
                libros.append(lote)
                
        except FileNotFoundError:
            print('Le pifiaste al archivo!')
         
        return libros

#%%  
# Ejercicio 2
def ingresos_por_genero(lista):
    lista_generos=list()
    total_compra=list()
    
    # para saber la cantidad de generos
    for i in range(0,len(lista)):
        item=lista[i]
        lista_generos.append(item['genero'])
        total_compra.append(item['precio']*item['cantidad'])
    
    set_generos_unicos=set(lista_generos)
    
    lista_generos_unicos=[]
    for i in set_generos_unicos:
        lista_generos_unicos.append(i)
    
    # para calcular total de generos
    total_item={}
    for conj in set_generos_unicos:
        total_item[conj]=0
    
    
    for i in range(0,len(lista)):
        item=lista[i]
        for conj in set_generos_unicos:
            if item['genero']==conj:
                total_item[conj]=int(total_item[conj])+item['precio']*item['cantidad']
    
        
    return total_item

#%%  
# Ejercicio 3
import sys

def generar_informe(nombre_archivo):
    libros=leer_ventas(nombre_archivo)
    total_item=ingresos_por_genero(libros)

    print('Ingresos por género:')
    
    for each in total_item.keys():
        print( each, total_item[str(each)])

    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'ventas.csv'
        
#%%  
# Print final
generar_informe(nombre_archivo)
