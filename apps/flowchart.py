import dash
import dash_cytoscape as cyto
from dash import html,dcc,Input, Output, Dash
import json
import dash_bootstrap_components as dbc
import pathlib


PATH = pathlib.Path(__file__).parent
DATA_PATH=(PATH.joinpath("../data")).resolve()


from app import app

#app = Dash(__name__)
#server = app.server


pre = {
        'border': 'thin white solid',
        'height': '100vh',
        "width": "30%",
        "background-color":"#14213d",
        "overflow-y":"scroll",
        "color": "white",
        "font-size":10,
        "font-family" : "Geneva",
        "display":"inline-block"
        
    }



#app = dash.Dash(__name__)



x_base = 50
y_base = 50
spacing = 50

elements = [
                # Parent Nodes
                {
                    'data': {'id': 'generation', 'label': 'Data Generation'},
                    "locked":True,
                    "classes": "sections"
                },
                {
                    'data': {'id': 'processing', 'label': 'Data Processing'},
                    "locked":True,
                    "classes": "sections"
                },
                {
                    'data': {'id': 'model', 'label': 'Galaxy Model'},
                    "locked":True,
                    "classes": "sections"
                },

                # Children Nodes
                {
                    'data': {'id': 'TNG', 'label': 'IllustrisTNG', 'parent': 'generation',"path": [f"{DATA_PATH}/assets/tng.png"]},
                    'position': {'x':x_base, 'y': y_base},
                    "locked":True,
                    "classes": "nodes image"
                },
                {
                    'data': {'id': 'load_data', 'label': 'Load Data', 'parent': 'generation',"size": 2},
                    'position': {'x': x_base, 'y': y_base + 50},
                    "locked":True,
                    "classes": "nodes"
                },
                {
                    'data': {'id': 'subhalo', 'label': 'Subhalo', 'parent': 'generation', "path": ['assets/subhalo.png']},
                    'position': {'x': x_base - spacing, 'y':  y_base + spacing},
                    "locked":True,
                    "classes": "nodes image"
                },
                
                {
                    'data': {'id': 'particles', 'label': 'Particles', 'parent': 'generation',"path": ["assets/particles.png"]},
                    'position': {'x':x_base + spacing, 'y':  y_base+spacing},
                    "locked":True,
                    "classes": "nodes image"
                },
                
                {
                    'data': {'id': 'SubhaloMass', 'label': 'Subhalo Mass', 'parent': 'generation',"size": 2},
                    'position': {'x': x_base - 2*spacing, 'y':  y_base + spacing},
                    "locked":True,
                    "classes": "variables"
                },
                  {
                    'data': {'id': 'SubhaloPosition', 'label': 'Subhalo Position', 'parent': 'generation',"size": 2},
                    'position': {'x':  x_base - 2*spacing, 'y': y_base + 2*spacing},
                    "locked":True,
                    "classes": "variables"
                },
                  
                  {
                    'data': {'id': 'SubhaloHalfMass', 'label': 'HalfMassRad', 'parent': 'generation',"size": 2},
                    'position': {'x': x_base -2*spacing , 'y': y_base},
                    "locked":True,
                    "classes": "variables"
                },
                  {
                    'data': {'id': 'ParticleCoordinates', 'label': 'Coordinates', 'parent': 'generation',"size": 2},
                    'position': {'x': x_base +2*spacing , 'y': y_base+2*spacing},
                    "locked":True,
                    "classes": "variables"
                },
                  
                  {
                    'data': {'id': 'ParticleHsml', 'label': 'Smoothing Length', 'parent': 'generation',"size": 2},
                    'position': {'x': x_base +2*spacing , 'y': y_base},
                    "locked":True,
                    "classes": "variables"
                },
                
                {
                    'data': {'id': 'ParticleMass', 'label': 'Particle Masses', 'parent': 'generation',"size": 2},
                    'position': {'x':  x_base + 2*spacing, 'y': y_base + spacing},
                    "locked":True,
                    "classes": "variables"
                },
                
                {
                    'data': {'id': 'inertia', 'label': 'Moment of Inertia Tensor', 'parent': 'generation',"size": 2},
                    'position': {'x':  x_base, 'y': y_base + 2*spacing},
                    "locked":True,
                    "classes": "nodes"
                },
                
                {
                    'data': {'id': 'rotationMatrix', 'label': 'Rotation Matrix', 'parent': 'generation',"size": 2},
                    'position': {'x':  x_base-100, 'y': y_base + 3*spacing},
                    "locked":True,
                    "classes": "nodes"
                },
                {
                    'data': {'id': 'FaceOn', 'label': 'Face On Rotation', 'parent': 'generation',"size": 2},
                    'position': {'x':  x_base, 'y': y_base + 3*spacing},
                    "locked":True,
                    "classes": "nodes"
                },
                {
                    'data': {'id': 'horzontalRotation', 'label': 'Horizontal Rotation', 'parent': 'generation',"size": 2},
                    'position': {'x': x_base +2*spacing , 'y': y_base+3*spacing},
                    "locked":True,
                    "classes": "nodes"
                },
                
                  {
                    'data': {'id': 'rotatedCoordinates', 'label': 'Rotated Coordinates', 'parent': 'generation',"size": 2},
                    'position': {'x': x_base+ 3*spacing, 'y': y_base+2*spacing},
                    "locked":True,
                    "classes": "variables"
                },
                {
                    'data': {'id': 'smoothedImages', 'label': 'Smoothed Images', 'parent': 'generation'},
                    'position': {'x': x_base+ 4*spacing, 'y': y_base+1*spacing},
                    "locked":True,
                    "classes": "nodes", 
                },
                
                  {
                    'data': {'id': 'rawimage', 'label': 'Raw Image', 'parent': 'processing', "path": ["assets/smoothed_image.png"]},
                    'position': {'x': x_base, 'y': y_base+6*spacing},
                    "locked":True,
                    "classes": "nodes image", 
                },
                
                {
                    'data': {'id': 'log', 'label': 'Log', 'parent': 'processing', "path": ["assets/logscale.png"]},
                    'position': {'x': x_base+ 1*spacing, 'y':  y_base+6*spacing},
                    "locked":True,
                    "classes": "nodes image", 
                },
                
                {
                    'data': {'id': 'noiseclip', 'label': 'Noise Clipping', 'parent': 'processing', "path": ["assets/noiseclipped.png"]},
                    'position': {'x': x_base+ 2*spacing, 'y':  y_base+6*spacing},
                    "locked":True,
                    "classes": "nodes image", 
                },
                
                  {
                    'data': {'id': 'norm', 'label': 'Norm', 'parent': 'processing'},
                    'position': {'x': x_base+ 1*spacing, 'y':  y_base+7*spacing},
                    "locked":True,
                    "classes": "nodes", 
                },
                  {
                    'data': {'id': 'masscut', 'label': 'Mass Cut', 'parent': 'processing'},
                    'position': {'x': x_base, 'y':  y_base+7*spacing},
                    "locked":True,
                    "classes": "nodes", 
                },
                  {
                    'data': {'id': 'meanpixel', 'label': 'Pixel Histogram', 'parent': 'processing'},
                    'position': {'x': x_base+2*spacing, 'y':  y_base+7*spacing},
                    "locked":True,
                    "classes": "nodes", 
                },
                  
                  
                {
                    'data': {'id': 'clean', 'label': 'Data Cleaning', 'parent': 'processing'},
                    'position': {'x': x_base+ 1*spacing, 'y':  y_base+8*spacing},
                    "locked":True,
                    "classes": "nodes", 
                },
                
                  
                {
                    'data': {'id': 'pca', 'label': 'PCA', 'parent': 'model'},
                    'position': {'x': x_base, 'y':  y_base+10*spacing},
                    "locked":True,
                    "classes": "nodes", 
                },
                {
                    'data': {'id': 'gan', 'label': 'GAN', 'parent': 'model'},
                    'position': {'x': x_base+2*spacing, 'y':  y_base+10*spacing},
                    "locked":True,
                    "classes": "nodes", 
                },
                
                
                # Edges
                {
                    'data': {'source': 'processing', 'target': 'generation', "label": "12,468 images"},
                    'classes': 'data_generation'
                },
                {
                    'data': {'source': 'generation', 'target': 'model', "label": "9,763 images"},
                    'classes': 'data_generation'
                },
                {
                    'data': {'source': 'TNG', 'target': 'load_data'},
                    'classes': 'data'
                },
                {
                    'data': {'source': 'load_data', 'target': 'particles'},
                    'classes': 'function'
                },
                {
                    'data': {'source': 'load_data', 'target': 'subhalo'},
                    'classes': 'function'
                }
                ,
                {
                    'data': {'source': 'subhalo', 'target': 'SubhaloMass'},
                    'classes': 'data'
                }
                ,
                {
                    'data': {'source': 'subhalo', 'target': 'SubhaloHalfMass'},
                    'classes': 'data'
                }
                ,
                {
                    'data': {'source': 'subhalo', 'target': 'SubhaloPosition'},
                    'classes': 'data'
                },
                
                {
                    'data': {'source': 'particles', 'target': 'ParticleCoordinates'},
                    'classes': 'data'
                }
                ,
                {
                    'data': {'source': 'particles', 'target': 'ParticleHsml'},
                    'classes': 'data'
                }
                ,
                {
                    'data': {'source': 'particles', 'target': 'ParticleMass'},
                    'classes': 'data'
                }
                ,
                {
                    'data': {'source': 'particles', 'target': 'inertia'},
                    'classes': 'input'
                }
                ,
                {
                    'data': {'source': 'subhalo', 'target': 'inertia'},
                    'classes': 'input'
                }
                ,
                {
                    'data': {'source': 'inertia', 'target': "rotationMatrix"},
                    'classes': 'input'
                }
                ,
                {
                    'data': {'source': 'rotationMatrix', 'target': "FaceOn"},
                    'classes': 'input'
                }
                  ,
                {
                    'data': {'source': 'ParticleCoordinates', 'target': "FaceOn"},
                    'classes': 'input'
                }
                ,
                {
                    'data': {'source': 'FaceOn', 'target': "horzontalRotation"},
                    'classes': 'input'
                },
                 {
                    'data': {'source': 'horzontalRotation', 'target': 'rotatedCoordinates'},
                    'classes': 'data'
                }
                 ,
                 {
                    'data': {'source': 'rotatedCoordinates', 'target': 'smoothedImages'},
                    'classes': 'input'
                }
                  ,
                 {
                    'data': {'source': 'ParticleMass', 'target': 'smoothedImages'},
                    'classes': 'input'
                }
                ,
                 {
                    'data': {'source': 'ParticleHsml', 'target': 'smoothedImages'},
                    'classes': 'input'
                }
                 ,
                 {
                    'data': {'source': 'rawimage', 'target': 'log'},
                    'classes': 'input'
                }
                 ,
                 {
                    'data': {'source': 'log', 'target': 'noiseclip'},
                    'classes': 'input'
                }
                 ,
                 {
                    'data': {'source': 'noiseclip', 'target': 'norm'},
                    'classes': 'input'
                }
                 ,
                 {
                    'data': {'source': 'masscut', 'target': 'clean'},
                    'classes': 'input'
                }
                 ,
                 {
                    'data': {'source': 'meanpixel', 'target': 'clean'},
                    'classes': 'input'
                }
                 ,
                 {
                    'data': {'source': 'norm', 'target': 'clean'},
                    'classes': 'input'
                }
                 
            
        
                ]

stylesheet = [{'selector': 'node',
              'style': {'content': 'data(label)','background-color': "white", "color":"white","width": "mapData(size, 0, 100, 20, 60)","height": "mapData(size, 0, 100, 20, 60)"}
                },
              {'selector': 'edge',
              'style': {"label": "data(label)","curve-style": "bezier","font-size": 10, "font-family" : "Geneva","color":"white","text-halign": "right"}
                },
              {'selector': '.sections',
                'style': {'width': 3,'background-color': "#A5C9CA","font-family":"Geneva", "curve-style":"bezier",'source-arrow-shape': 'triangle-backcurve',"shape": "roundrectangle"},
                },{
                    'selector': '.function',
                    'style': {'line-style': 'dashed',"width": 2,"line-color": "#0077b6",'target-arrow-shape': 'triangle',"target-arrow-color": "#0077b6"}
                },{
                    'selector': '.data',
                    'style': { "line-color": "orange", "target-arrow-color": "orange","curve-style":"bezier", "width":2}
                },{
                    'selector': '.nodes',
                    'style': {"font-size": 10, "font-family" : "Geneva","shape": "roundrectangle", "background-color": "#e8c2ca","width":15, "height": 15,
                              }
                },{
                    'selector': '.variables',
                    'style': {"font-size": 5, "font-family" : "Geneva", "shape": "diamond", "background-color":"#EC8FD0"}
                },
                {
                    'selector': '.input',
                    'style': { "line-color": "red","target-arrow-shape": "triangle-backcurve", "target-arrow-color": "red","curve-style":"bezier", "width":1, "arrow-scale":1}
                },
                {
                    'selector': '.image',
                    'style': {
                        "width":25, "height":25,
                        "background-image": "data(path)",
                        }
                },
               ]
 
 

layout =html.Div( children = [
    

        cyto.Cytoscape(
                        id='cytoscape-compound',
                        layout={'name': 'preset'},
                        stylesheet=stylesheet,
                        elements=elements,
                        style={'width': '70%','height': '100vh',"background-color":"#14213d", "display":"inline-block"},
                        ),

             dcc.Markdown('''#Click a Node to see more Information here!''',id='cytoscape-tapNodeData-json',highlight_config={"theme":"dark"}, style=pre),                
], style ={"display":"flex", "align-items":"flex-end"} )
  
@app.callback(Output('cytoscape-tapNodeData-json', 'children'),
              Input('cytoscape-compound', 'tapNodeData'))
def displayTapNodeData(data):
    if data is None:
        return("Click on a Node to show more Information here!")
    #open text file in read mode
    text_file = open(f"docs/{data['id']}.md", "r")
    
    #read whole file to a string
    data = text_file.read()
    
    #close file
    text_file.close()
    return data





