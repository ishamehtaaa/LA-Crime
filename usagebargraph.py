## classifying weapon usage by area: 

# for each weapon, find out how much it was used in each area.

#create bar graphs using areas as x acis - each area is a sliver on teh x axis, and
# the count of the weapon is the y axis, create as many graphs 

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

def create_bar_graph(weapon_name):
    item = weapon.str.contains(str(weapon_name))
    item = data[item == True]
    k = item["AREA NAME"]
    sw = {}
    for i in k:
        if i in sw:
            sw[i] += 1
        else:
            sw[i] = 1
    return sw

print(create_bar_graph("ROCK/THROWN OBJECT"))
