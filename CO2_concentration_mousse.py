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
file_path3='/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test-colonne-3d-co2-15-2.csv'
file_path4='/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test-colonne-3d-co2-15-vidange-2.csv'

db=pd.read_csv(file_path)
db2=pd.read_csv(file_path2)
db3=pd.read_csv(file_path3)
db4=pd.read_csv(file_path4)

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


xdata3=db3.index/2  ### TEST 2 REMPLISSAGE
popt3, pcov3=curve_fit(func2, xdata3, db3['Media concentration value']/100)
popt3
#### CO2 VIDANGE FIT
xdata2=db2.index/2 ### TEST 1 VIDANGE
popt2, pcov2=curve_fit(func, xdata2, db2['Media concentration value']/100)
popt2

xdata4=db4.index/2  #### TEST 2 VIDANGE
popt4, pcov4=curve_fit(func, xdata4, db4['Media value concentration']/100)
popt4






plt.figure()
plt.scatter(db.index/2, db['Media concentration value']/100, label='Test_1 remplissage', marker='o', s=2)
plt.scatter(db2.index/2, db2['Media concentration value']/100, label='Test_1 vidange', marker='o', s=2)
plt.plot(xdata, func2(xdata, *popt), 'k-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt))
plt.plot(xdata2, func(xdata2, *popt2), 'r-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt2))
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.legend()
plt.title('Test 1 colonne 3D remplissage et vidange du CO2 15% debit', fontsize=20)
plt.show()

plt.figure()
plt.scatter(db3.index/2, db3['Media concentration value']/100, label='Test_2 remplissage', marker='o', s=2)
plt.scatter(db4.index/2, db4['Media value concentration']/100, label='Test_2 vidange', marker='o', s=2)
plt.plot(xdata3, func2(xdata3, *popt3), 'k-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt3))
plt.plot(xdata4, func(xdata4, *popt4), 'r-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt4))
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.legend()
plt.title('Test 2 colonne 3D remplissage et vidange du CO2 15% debit', fontsize=20)
plt.show()