




from dash import html,dcc,Input, Output, Dash,no_update


import pathlib
import numpy as np
import plotly.graph_objects as go
from PIL import Image

PATH = pathlib.Path(__file__).parent
DATA_PATH= PATH.joinpath("data").resolve()
IMAGE_PATH = DATA_PATH.joinpath("masses")


df = np.load(DATA_PATH.joinpath("umap_embedding.npy"))


log_masses = np.load(DATA_PATH.joinpath("log_masses.npy"))
halo_ids = np.load(DATA_PATH.joinpath("halo_ids.npy"))
x_dat = df[:,0]
y_dat = df[:,1]


size_norm = 600
color_bar = "log10(M/M_sun)"



masses = log_masses
color = masses.copy()
color = (color - color.min())/color.max()
color =masses
fig = go.Figure(data=[
    go.Scatter(
        x=x_dat,
        y=y_dat,
        mode="markers",
        marker=dict(
            colorscale="viridis",
            color=color,
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

    # Get halo_id of corresponding point
    halo_id = halo_ids[num]
    #df_row = df.iloc[num]
    #img_src = df_row['IMG_URL']
    img_src = Image.open(f"{IMAGE_PATH}/masses_{str(num)}.png")
    #img_src = f"https://ufuk-bachelor-thesis.s3.eu-west-2.amazonaws.com/plotly_images/{str(num).zfill(5)}.png"
    name = f"TNG ID: {halo_ids[num]}"
    
    #if len(desc) > 300: desc = desc[:100] + '...'
    
    children = [
        html.Div(children=[
            html.Img(src=img_src,alt="image", style={"width": "100%"}),
            html.H2(f"{name}", style={"color": "darkblue"}),
        ],
        style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, bbox, children




if __name__ == "__main__":
    app.layout = layout
    app.run_server(host='0.0.0.0', port=10000)




