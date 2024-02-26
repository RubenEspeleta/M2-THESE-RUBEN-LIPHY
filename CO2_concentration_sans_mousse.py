#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:48:30 2024

@author: ruben
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_path='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_100_co2.csv'
file_path2='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_co2-vidage.csv'
file_path3='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_100_co2-2.csv'
file_path4='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_co2-vidage-2.csv'
db=pd.read_csv(file_path)
db2=pd.read_csv(file_path2)
db3=pd.read_csv(file_path3)
db4=pd.read_csv(file_path4)
plt.plot(db.index, db['Media value concentration']/100, label='Test_1 concentration')
plt.plot(db2.index, db2['Media value concentration']/100, label = 'Test_1 emptying')

plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.legend()
plt.show()

plt.figure()
plt.plot(db3.index, db3['Media value concentration']/100, label='Test_2 concentration')
plt.plot(db4.index, db4['Media value concentration']/100, label='Test_2 emptying')

plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.legend()
plt.show()
    
    
