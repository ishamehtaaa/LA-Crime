import weaponmain as wp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# weapon distribution for central:
central = wp.area.str.contains("Central") 
central = wp.data[central == True] # only view rows that take place in central 

print(len(central))

# get frequency of each weapon and how many times it was used 
k = central["Weapon Desc"]
central_weapons = {}
for i in k:
    if i in central_weapons:
        central_weapons[i] += 1
    else:
        central_weapons[i] = 0

# if frequency was less than 10% of overall crime in Central, don't include:
cweap = {}
for weapon_desc, count in central_weapons.items():
    if count > 200:
        cweap[weapon_desc] = count
    else:
        continue

# turn weapons and frequencies into series
pl = []
pv = []
for i in cweap.keys():
    pl.append(i) 
for j in cweap.values():
    pv.append(j)
pv = pd.Series(pv)
pl = pd.Series(pl)

# feed series into pie chart parameters
numbers = pl
quantity = pv

fig = px.pie(central, values = quantity, names=numbers)
fig.show()
