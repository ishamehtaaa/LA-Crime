import weaponmain as wp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


#g = wp.top10cities[:5]
"""
for i in g:
    print(wp.create_crime_graph(str(i)))

"""


slay = input("Please input the county you wish you obtain a crime graph for? ")
print(wp.create_crime_graph(slay))
