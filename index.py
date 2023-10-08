from dash import Dash, dcc, html, Input, Output

# Connect to main app.py File
from app import app
from app import server


from apps import eigen, flowchart, umap

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])




@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/flowchart':
        return flowchart.layout
    if pathname == '/apps/eigen':
        return eigen.layout
    if pathname == '/apps/umap':
        return umap.layout
    else:
        return eigen.layout


if __name__ == '__main__':
    app.run_server(debug=False)


from apps import eigen, umap

