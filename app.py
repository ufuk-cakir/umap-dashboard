




from dash import html,dcc,Input, Output, Dash,no_update


import pathlib
import numpy as np
import plotly.graph_objects as go
from PIL import Image

PATH = pathlib.Path(__file__).parent
DATA_PATH= PATH.joinpath("data").resolve()
IMAGE_PATH = DATA_PATH.joinpath("plotly_images")


df = np.load(DATA_PATH.joinpath("umap_data.npy"), allow_pickle=True).item()

x_dat = df["umap"][:,0]
y_dat = df["umap"][:,1]


size_norm = 600
color_bar = "Mass"

size = size_norm*df["p_late"]


masses = df["Mass"]
masses = masses - masses.min()
masses = masses/masses.max()

color =masses

fig = go.Figure(data=[
    go.Scatter(
        x=x_dat,
        y=y_dat,
        mode="markers",
        marker=dict(
            colorscale="viridis",
            color=color,
            size=size,
            colorbar={"title": color_bar},
            line={"color": "#444"},
            reversescale=True,
            sizeref=45,
            sizemode="diameter",
            opacity=0.8,
        
        )
    )
])

fig.update_traces(hoverinfo="none", hovertemplate=None)

fig.update_layout(
    xaxis=dict(title='UMAP x'),
    yaxis=dict(title='UMAP y'),
    plot_bgcolor='rgba(255,255,255,0.1)'
)


#from app import app

#app = Dash(__name__)

app = Dash(__name__)
server = app.server

layout = html.Div([
    dcc.Graph(id="graph", figure=fig, clear_on_unhover=True,style={'width': '100vw', 'height': '100vh'}),
    dcc.Tooltip(id="graph-tooltip")
])

app.layout = layout

@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Input("graph", "hoverData"),
)

def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    # demo only shows the first point, but other points may also be available
    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]

    #df_row = df.iloc[num]
    #img_src = df_row['IMG_URL']
    img_src = Image.open(f"{IMAGE_PATH}/{str(num).zfill(5)}.png")
    #img_src = f"https://ufuk-bachelor-thesis.s3.eu-west-2.amazonaws.com/plotly_images/{str(num).zfill(5)}.png"
    name = f"TNG ID: {df['halo_ids'][num]}"
    ellip = f"Late Type Probability: {round(df['p_late'][num],2)}"
    mass = f"Mass: {round(df['Mass'][num],2)}*10^10 M_sun"
    #if len(desc) > 300: desc = desc[:100] + '...'
    
    children = [
        html.Div(children=[
            html.Img(src=img_src,alt="image", style={"width": "100%"}),
            html.H2(f"{name}", style={"color": "darkblue"}),
            html.P(f"{ellip}"),
            html.P(f"{mass}"),
        ],
        style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, bbox, children




if __name__ == "__main__":
    app.layout = layout
    app.run_server(debug=True)




