# LA Crime by Area

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


data.drop(to_drop, inplace=True, axis=1)
data = data.dropna()
area = data["AREA NAME"]
weapon = data["Weapon Desc"]

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

    fig = px.pie(sector, values = quantity, names=numbers, title=str(sector_name))
    fig.update_layout(
        font_color="red"
    )
    fig.show()

