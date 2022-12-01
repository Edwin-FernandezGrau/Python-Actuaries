# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:15:59 2021

@author: DELL
"""
#!/usr/bin/env python
# coding: utf-8


# In[19]:


# importar un módulo de funciones creado por usted mismo
import Funact as fa
import pandas as pd


life_table = pd.read_excel("life_table.xlsx",engine='openpyxl')
temporales = pd.read_excel("temporales.xlsx",engine='openpyxl')

# aplicamos la función para todos los clientes
#temporales["prima"] =  [fa.temp_life(temporales.age[x] ,temporales.n[x],temporales.i[x],life_table)*temporales.benefit[x] for x in range(len(temporales))]



polizas = {}
for x in range(len(temporales)):
   polizas["{}".format(temporales.nro_cliente[x])] = fa.poltemp(temporales.nro_cliente[x],temporales.age[x],temporales.n[x],temporales.i[x],temporales.benefit[x])
               
               
polizas["20"].resumen