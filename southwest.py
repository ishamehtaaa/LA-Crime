import weaponmain as wp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

k = []
for i in wp.areacount.keys():
    k.append(i)
#g = wp.top10cities[:5]
"""
for i in g:
    print(wp.create_crime_graph(str(i)))

"""
print(wp.create_crime_graph("West LA"))
