#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 11:11:44 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

file_path='/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test-colonne-3d-co2-15.csv'
file_path2='/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test-colonne-3d-co2-15-vidange.csv'
db=pd.read_csv(file_path)
db2=pd.read_csv(file_path2)

#### CO2 REMPLISSAGE ####
def func2(x, a, b, c, phi):
    return a/(1+((a-c)/c)*np.exp(-b*x+phi)) 


#### CO2 VIDANGE #######
def func(x, a, b, c, phi):
    return a*np.exp(-b*x+phi)+c

#### CO2 REMPLISSAGE FIT
xdata=db.index/2   #### TEST 1 REMPLISSAGE
popt, pcov=curve_fit(func2, xdata, db['Media concentration value']/100)
popt

#### CO2 VIDANGE FIT
#xdata2=db2.index/2 ### TEST 1 VIDANGE






plt.figure()
plt.scatter(db.index/2, db['Media concentration value']/100, label='Test_1 concentration', marker='o', s=2)
plt.plot(xdata, func2(xdata, *popt), 'k-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f, phi=%5.3f ' % tuple(popt))
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.legend()
plt.title('Test 1 colonne 3D remplissage du CO2 15% debit', fontsize=20)
plt.show()