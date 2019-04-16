#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    import os
    import sys
    import csv
    import time

except Exception as E:
    print('\n001 - Erro ao importar bibliotecas.\n')
    print(str(E))


# [ Abre arquivo CSV ".csv" ou Texto ".txt", delimitado por ";", e le os dados dele ]
try:
    with open("arquivo.csv", encoding="Latin-1") as csvDataFile:
        data = [row for row in csv.reader(csvDataFile, delimiter=';')]

except Exception as E:
    print('\n002 - Erro ao capturar arquivo CSV.\n')
    print(str(E))

    
# [ Loop para printar os dados do CSV *POR CELULA* ]
print("\nPor Celula:")   
try:
    for row in range(1, len(data)):
        for column in range (0, 2):
            try:
                print(str(data[row][0]))  

            except Exception as E:
                print('\n003 - Erro ao Printar os valores das celulas do Excel.\n')
                print(str(E))

except Exception as E:
    print('\n004 - Erro ao Executar o Loop.\n')
    print(str(E))
     
        
# [ Loop para printar os dados do CSV *POR ROW* ]
print("\nPor Row:")  
try:
    for row in data:
        try:
            print(row)  

        except Exception as E:
            print('\n005 - Erro ao Printar os valores das celulas do Excel.\n')
            print(str(E))

except Exception as E:
    print('\n006 - Erro ao Executar o Loop.\n')
    print(str(E))
    
    
time.sleep(30)