import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")

to_drop = [
    "DR_NO",
    "Date Rptd", 
    "DATE OCC",
    "TIME OCC",
    "Rpt Dist No", 
    "Part 1-2", 
    "Mocodes",
    "Premis Cd",
    "Status", 
    "Status Desc",
    "Crm Cd 1",
    "Crm Cd 2",
    "Crm Cd 3",
    "Crm Cd 4",
    "LOCATION",
    "Cross Street", 
    "LAT",
    "LON"
]

area = data["AREA NAME"]
weapon = data["Weapon Desc"]


data.drop(to_drop, inplace=True, axis=1)
data = data.dropna()

areacount = {}
for i in area:
    if i in areacount:
        areacount[i] += 1
    else:

        areacount[i] = 0

weaponcount = {}
for k in weapon:
    if k in weaponcount:
        weaponcount[k] += 1
    else:
        weaponcount[k] = 0
"""
central = area.str.contains("Central")
central = data[central == True]

k = central["Weapon Desc"]
central_weapons = {}
for i in k:
    if i in central_weapons:
        central_weapons[i] += 1
    else:
        central_weapons[i] = 1

sorted_weapons = sorted(central_weapons.items(), key = lambda x:x[1], reverse=True)
print(sorted_weapons)

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

fig = px.pie(central, values = quantity, names=numbers, title="Central",  color_discrete_sequence=px.colors.qualitative.Pastel1)
fig.show()

"""
def create_crime_graph(sector_name):    
    sector = area.str.contains(str(sector_name))
    sector = data[sector == True]
    k = sector["Weapon Desc"]
    sector_weapons = {}
    for i in k:
        if i in sector_weapons:
            sector_weapons[i] += 1
        else:
            sector_weapons[i] = 0
    freq_stats = {}
    negligible = (len(sector) / 100)
    for weapon_desc, count in sector_weapons.items():
        if count > negligible:
            freq_stats[weapon_desc] = count
        else:
            continue
    pl = []
    pv = []
    for i in freq_stats.keys():
        pl.append(i) 
    for j in freq_stats.values():
        pv.append(j)
    pv = pd.Series(pv)
    pl = pd.Series(pl)
    numbers = pl
    quantity = pv

    fig = px.pie(sector, values = quantity, names=numbers, title=str(sector_name),  color_discrete_sequence=px.colors.qualitative.Pastel1)
    fig.update_layout(
        font_color="red"
    )
    fig.show()


print(create_crime_graph("Mission"))

for i in areacount:
    print(create_crime_graph(i))
