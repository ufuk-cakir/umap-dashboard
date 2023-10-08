from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pathlib


from app import app
#app = Dash(__name__)
#server = app.server

PATH = pathlib.Path(__file__).parent
DATA_PATH=(PATH.joinpath("../data")).resolve()



eigengalaxies = np.load(DATA_PATH.joinpath("new_eigen.npy"))

def normalize(arr):
    arr_min = np.min(arr[np.isfinite(arr)])
    scale_arr = np.zeros_like(arr)
    scale_arr[np.isfinite(arr)] = (arr[np.isfinite(arr)]-arr_min)/(np.max(arr[np.isfinite(arr)])-arr_min)
    return scale_arr





eigen_index = 4
min_val = 1e-5
norm = False
cmap = "magma"

opacity = .1
surface_count = 25


data = eigengalaxies[eigen_index].copy()
if norm: data = normalize(data)
xx, yy, zz = np.where(data != 0)

s = data[xx,yy,zz]
isomin = s.min()
isomax = s.max()


fig_eigen = go.Figure(data = [go.Volume(
    x=xx,
    y=yy,
    z=zz,
    value=s,
    isomin=isomin,
    isomax=isomax,
    opacity=opacity, # needs to be small to see through all surfaces
    surface_count=surface_count,
    colorscale=cmap
)])
fig_eigen.update_layout(title_text=f"Eigengalaxy Number: {eigen_index}")



layout = html.Div([
    dcc.Dropdown(id = "dropdown_eigen",options = [dict(label= f"{i}",value = f"{i}") for i in range(len(eigengalaxies))],
                disabled = False, multi = False, placeholder="Select Eigengalaxy...",optionHeight=25, value = 4),
    dcc.Graph(id="eigengalaxies_graph", figure=fig_eigen, clear_on_unhover=True,style={'width': '90vw', 'height': '90vh'}),
    dcc.Tooltip(id="eigengalaxies_graph-tooltip"),
])


@app.callback(Output("eigengalaxies_graph", "figure"),
              Input("dropdown_eigen", "value"))
def update_graph(dropdown_eigen):
    data = eigengalaxies[int(dropdown_eigen)].copy()
    #data[np.where(data <min_val)] = 0
    #if norm: data = normalize(data)
    xx, yy, zz = np.where(data != 0)
    s = data[xx,yy,zz]
    fig = go.Figure(data = [go.Volume(
    x=xx,
    y=yy,
    z=zz,
    value=s,
    isomin=s.min(),
    isomax=s.max(),
    opacity=opacity, # needs to be small to see through all surfaces
    surface_count=surface_count,
    colorscale = cmap 
)])
    fig.update_layout(title_text=f"Eigengalaxy Number: {int(dropdown_eigen)}")
    return(fig)
    

