
# In[3]:

import pandas as pd
import numpy as np

life_table = pd.read_excel("life_table.xlsx",engine='openpyxl') 

# In[ ]:

def whole_life(age,i,life_table):
    ''' Construya un seguro de vida completo, tomando como insumos la edad, tasas interes y tabla de mortalidad'''
    qx = life_table.qx
    px = 1- qx
    
    kpx = pd.concat( [pd.Series(1), np.cumprod(px[age:len(px)-1])  ] ,ignore_index= True ) 
    
    qxs = (qx[(age):len(qx)])
    qxs.reset_index(inplace=True,drop = True)
    
    kqx = kpx*qxs
    
    per = len(kpx)
    exp = pd.Series(range(1,per+1))
    discount_factor =  (1 + i)**-(exp)

    return sum(discount_factor * kqx)
    
    


# In[ ]:


def temp_life(age,n,i,life_table):
    ''' Construya un seguro de vida temporal, tomando como insumos la edad, temporalidad, tasas interes y tabla de mortalidad'''
    
    qx = life_table.qx
    px = 1- qx
    
    kpx = pd.concat( [pd.Series(1), np.cumprod(px[age:age+n-1])  ] ,ignore_index= True ) 
    
    qxs = (qx[age:age+n])
    qxs.reset_index(inplace=True,drop = True)
    
    kqx = kpx*qxs
    
    per = len(kpx)
    exp = pd.Series(range(1,per+1))
    discount_factor =  (1 + i)**-(exp)

    return sum(discount_factor * kqx)



# In[ ]:

def dif_life(age,u,i,life_table):

    ''' Construya una función que calcule el EPV de un seguro de vida entera diferido, tomando como insumos la edad, per diferidos, tasas interes y tabla de mortalidad.'''
    qx = life_table.qx
    px = 1- qx
    
    kpx = pd.concat( [pd.Series(1), np.cumprod(px[age:len(px)-1])  ] ,ignore_index= True ) 
    
    qxs = (qx[(age):len(qx)])
    qxs.reset_index(inplace=True,drop = True)
    
    kqx = kpx*qxs
    
    per = len(kpx)
    exp = pd.Series(range(1,per+1))
    discount_factor =  (1 + i)**-(exp)

    benefits = pd.Series([0]*u + [1]*(len(kpx)-u) )
    return sum(benefits*discount_factor * kqx)




class poltemp:

    def __init__(self,nro,age,n,i,benefit):
        self.nro = nro
        self.age = age
        self.n = n
        self.i = i
        self.benefit = benefit
        self.prima =  temp_life(self.age,self.n,self.i,life_table)*self.benefit
        self.resumen = "La poliza {} corresponde a un seguro de vida para una persona de {} años con temporalidad {} ,tasa de {} y un beneficio de {}.La prima es {}".format(self.nro, self.age, self.n, self.i, self.benefit,self.prima)




