'''
Created on 31/08/2012

@author: Tomas B. Gonzalez Z.
'''
import os

crom = input("Ingrese el cromosoma que quiere evaluar (como número, del 1 al 22, o X o Y) :")
poblacion_1 = input("Ingrese el nombre de la poblacion 1 a evaluar.\n(ASW, CEU, CHB, CHD, GIH, JPT, LWK, MEX, MKK, TSI, YRI): ")


print("Programa para evaluar diferencias alelicas entre 2 poblaciones \n")
#ingresar primer archivo y su separador
nombre = input("Ingrese nombre del primer archivo: ")
separador = input ("Ingrese el separador de las columnas del primer archivo: ")

#Verificar si esxite el fichero
if os.path.exists(nombre):
    print("Carga exitosa")
else: #Si no existe, aparece siguiente linea
    print("Siga participando")    

#ingresar segundo archivo
nombre2 = input("\nIngrese nombre del primer archivo: ")
separador2 = input ("Ingrese el separador de las columnas del primer archivo: ")
    
#Verificar si esxite el segundo fichero
if os.path.exists(nombre2):
    print("Carga exitosa")
else: #Si no existe, aparece siguiente linea
    print("Siga participando")    

#Abrir el archivo por columnas
with open(nombre) as f1, open(nombre) as f2:
    a = {}
    for line in f1:
        a_snp, a_freq = line.split(separador)
        a[a_snp] = a_freq
    b = {}
    for line in f2:
        b_snp, b_freq = line.split(separador)
        b[b_snp] = b_freq
 
#Se escribe el primer archivo (output.txt) con los snp's coincidentes y sus dos frecuencias poblacionales            
with open("output.txt","w") as out1:
    for outline in [a[0]+"\t"+a[1]+"\t"+b[1] \
                    for a in [line.strip("\n").split(" ") \
                    for line in open("a.txt","r").readlines()] \
                    for b in [line.strip("\n").split(" ") \
                    for line in open("b.txt","r").readlines()] \
                    if a[0] == b[0]]:

                        out1.write(outline+"\n")
                        
#Verificar si esxite el archivo output.txt
if os.path.exists("output.txt"):
    input("\nFichero output.txt creado, presione enter para cerrar")
else: #Si no existe, aparece siguiente linea
    input("\nOcurrio un error, presione enter para cerrar")    

#Se escribe el archivo final, con la interseccion y la resta de las frecuencias de ambas poblaciones
#Se lee el archivo creado antes, se restan columnas y se genera nuevo archivo    
with open("output.txt", "r") as finput, open("outputf.txt", "w") as output:
    for linea in finput:
        columnas = linea.strip().split('\t')
        snp = columnas[0]
        freq1 = columnas[1]
        freq2 = columnas[2]
        delta = (float(columnas[1]) - float(columnas[2]))
        output.writelines(snp+'\t'+freq1+'\t'+freq2+'\t'+str(delta)+'\n')
finput.close()
output.close()

#Se comprueba si archivo final fue creado
if os.path.exists("outputf.txt"):
    input("\nFichero outputf.txt creado, presione enter para cerrar")
else: #Si no existe, aparece siguiente linea
    input("\nOcurrio un error, presione enter para cerrar")    
    
