#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:37 2018

@author: mike
"""
import mydcc
import plotly.graph_objs as go
import numpy as np
import dash 
import dash_core_components as dcc
import dash_html_components as html

xdiv=100
tdiv=50
#xmin=0
#xmax=10
#zmin=-2
#zmax=2
### Make the rectangular grid, the surface of the dented cylinder
theta = np.linspace(0,2*np.pi,tdiv) 
x = np.linspace(0,10,xdiv) 


tg,xg = np.meshgrid(theta,x) # grided versions

z = np.full((xdiv,tdiv),np.nan)
y = 2*np.cos(tg)

for dx in range(xdiv): # iterating x-coordinates
    for s in range(tdiv): # iterating theta-coordinates
        if theta[s] < 3*np.pi/2.: # 3/4 of the cylinder is perfect
           #if 2*np.sin(theta[s]) <= zthresh: #check
               z[dx,s] = 2*np.sin(theta[s])
        elif x[dx] <= 1 or x[dx] >= 9: #make the caps of the cylinder
            #if 2*np.sin(theta[s]) <= zthresh:
                 z[dx,s] = 2*np.sin(theta[s])
        elif 1<x[dx]<=3: # begin the deformation
            #if ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((x[dx]-1)/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(x[dx]-1)/2) <= zthresh:    
                z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((x[dx]-1)/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(x[dx]-1)/2)
        elif 3<x[dx]<=5: # wrinkle   
            #if ((1/14.)+(6/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)-1 <= zthresh:
                z[dx,s] = ((1/14.)+(6/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)-1
        elif 5<x[dx]<=7: # wrinkle
            #if ((1/14.)+(6/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)-1 <= zthresh:
                z[dx,s] = ((1/14.)+(6/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)-1
        elif 7<x[dx]<=9: # end the dent
            #if ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((9-x[dx])/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(9-x[dx])/2) <= zthresh:
                z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((9-x[dx])/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(9-x[dx])/2)



contours = dict(
        x=dict(
                show=False,
                highlight=False,
                usecolormap=False,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        y=dict(
                show=False,
                highlight=False,
                usecolormap=True,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        z=dict(
                show=False,
                highlight=True,
                usecolormap=True,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        )
s1 = go.Surface(x=xg,y=y,z=z,opacity=0.7,surfacecolor='cmocean',contours=contours,showscale=False)

################
app = dash.Dash()

app.layout = html.Div([
                 html.Div([ ## main div element for cylinder and vertical slider
                    html.Div([
                            mydcc.Relayout(id='rrr',aim='surface-cyl'),
                            dcc.Graph(id='surface-cyl',
                                      figure = { 'data': [s1],
                                                'layout': {
                                                    'showlegend':False,
                                                'scene': dict(
                                                       zaxis=dict(
                                                              showspikes=False,
                                                              range=[-2,2]),
                                                       xaxis=dict(
                                                              showspikes=False,
                                                              range=[0,10]),
                                                       yaxis=dict(
                                                              showspikes=False))}
                        }
                                                    )],
                              style={'height':'100%','width':'89%','display':'inline-block','padding':'50px 50px 50px 50px'}), 
        html.Div([dcc.RangeSlider(
                        id='z-slider',
                        min=-2,
                        max=2,
                        step=0.01,
                        marks=[i for i in range(-2,3)],
                        value=[-2 ,2],
                        vertical=True,
                        updatemode='drag',
                        allowCross=False,
                        )],
                style={'width':'10mm', 'height':'60mm','display':'inline-block','padding':'20px 20px 0px 0px'})
        ],style={'width':'90%','height':'100mm','padding':'0px 5px'}),
        html.Div([
                dcc.RangeSlider(
                        id='x-slider',
                        min=0,
                        step=0.01,
                        marks=[i for i in range(11)],
                        max=10,
                        value=[0,10],
                        allowCross=False,
                        updatemode='drag',
                        )
                ],style={'width':'60%'})
        ],style={'width':'100%','height':'100%'})
                
                # style would go here.
#        html.Div([ ## div element for Cerf diagram
#                ])
#style={'width' : ' 100%', 'display' : 'inline-block'})

#@app.callback(
#        dash.dependencies.Output('surface-cyl','figure'),
#        [dash.dependencies.Input('z-slider','value'),
#         dash.dependencies.Input('x-slider','value')])
#def update_figure(zval,xval):
#    return {
#            'data' : [s1],
#            'layout' : go.Layout(
#                    showlegend=False,
#                    #title='Dented Cylinder',
#                    scene= dict(
#                            aspectratio=dict(
#                               x=1.84296,y=0.73642,z=0.73680),
#                            zaxis=dict(
#                                    showspikes=False,
#                                    range=zval),
#                            xaxis=dict(
#                                    showspikes=False,
#                                    range=xval),
#                            yaxis=dict(
#                                    showspikes=False)
#                            )
#                        )
#            }


##### Modifications below, usual above
@app.callback(
        dash.dependencies.Output('rrr','layout'),
        [dash.dependencies.Input('z-slider','value'),
         dash.dependencies.Input('x-slider','value')])
def update_figure(zval,xval):
    return {'showlegend':False,
                    #title='Dented Cylinder',
                    'scene': dict(
                            zaxis=dict(
                                    showspikes=False,
                                    range=zval),
                            xaxis=dict(
                                    showspikes=False,
                                    range=xval),
                            yaxis=dict(
                                    showspikes=False)
                            )
                        }







#### Set the layout params
#
#layout = go.Layout(
#    title='Dented Cylinder with Threshold',
##    scene=dict(
 #       #aspectratio=dict(
        #    x=1.84296,y=0.73642,z=0.73680),
#        zaxis = dict(
#            range=[zmin,zmax]),
#        xaxis = dict(
#                range=[xmin,xmax])
#            ),
#
#)

#fig = go.Figure(data=[s1], layout=layout)
#py.iplot(fig, filename='Parametric_plot')
#plotly.offline.plot(fig,filename='Dented_cylinder_threshold_'+str(zmax)+'.html')
        
if __name__ == '__main__':
    app.run_server()