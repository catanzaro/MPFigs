#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

This code creates an html file, plotting the x = const slices of the wrinkled cylinder.
"""
import plotly
import plotly.graph_objs as go
import numpy as np

## Grid parameters
xdiv=100 
tdiv=50
## Make the rectangular grid, the surface of the dented cylinder
theta = np.linspace(0,2*np.pi,tdiv) 
x = np.linspace(0,10,xdiv) 

## Plotting parameters. These vary the 'level' and 'sublevel' spaces shown.
zval = [-2,2] # max [-2,2]
yval=[-2,2] # max [-2,2]
xval = [0,10] # max [0,10]

tg,xg = np.meshgrid(theta,x) # grid versions

z = np.full((xdiv,tdiv),np.nan)
y = 2*np.cos(tg)

for dx in range(xdiv): # iterating x-coordinates
    for s in range(tdiv): # iterating theta-coordinates
        if theta[s] < 3*np.pi/2.: # 3/4 of the cylinder is an actual cylinder
               z[dx,s] = 2*np.sin(theta[s])
        elif x[dx] <= 1 or x[dx] >= 9: #make the caps of the cylinder
                 z[dx,s] = 2*np.sin(theta[s])
        elif 1<x[dx]<=3: # begin the deformation
                z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((x[dx]-1)/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(x[dx]-1)/2)
        elif 3<x[dx]<=5: # wrinkle   
                z[dx,s] = ((1/14.)+(6/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)-1
        elif 5<x[dx]<=7: # wrinkle
                z[dx,s] = ((1/14.)+(6/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)-1
        elif 7<x[dx]<=9: # end the dent
                z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((9-x[dx])/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(9-x[dx])/2)


## Contour parameters: What to show on hover, etc.
#contours = dict(
#        x=dict(
#                show=False,
#                highlight=True,
#                highlightcolor='black',
#                highlightwidth=10,
#                usecolormap=False,
#                project=dict(
#                        x=False,
#                        y=False,
#                        z=False)),
#        y=dict(
#                show=False,
#                highlight=False,
#                usecolormap=True,
#                project=dict(
#                        x=False,
#                        y=False,
#                        z=False)),
#        z=dict(
#                show=False,
#                highlight=False,
#                usecolormap=True,
#                project=dict(
#                        x=False,
#                        y=False,
#                        z=False)),
#        )
#s1 = go.Surface(x=xg,y=y,z=z,opacity=0.7,surfacecolor='cmocean',contours=contours,showscale=False,hoverinfo='none')
traces=[]
for i in range(10): #iterate over x-values
    traces.append(go.Scatter3d(x=np.full((1,100),x[i*9]),y=y[i*9],z=z[i*9],line=dict(width=1)))


### Set the layout params

layout = go.Layout(
    title='Slices of wrinkled cylinder',
    scene=dict(
        aspectratio=dict(
            x=2,y=1,z=1),
        zaxis = dict(
            showspikes=False,
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title='',
            range=zval),
        xaxis = dict(
                showspikes=False,
                range=xval,
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                ticks='',
                title = '',
                showline=False),
        yaxis=dict(
                range=yval,
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                showspikes=False,
                ticks='',
                showline=False,
                title=''))
#    scene=dict(
#        xaxis=dict(
#            gridcolor='rgb(255, 255, 255)',
#            zerolinecolor='rgb(255, 255, 255)',
#            showbackground=True,
#            backgroundcolor='rgb(230, 230,230)'
#        ),
#        yaxis=dict(
#            gridcolor='rgb(255, 255, 255)',
#            zerolinecolor='rgb(255, 255, 255)',
#            showbackground=True,
#            backgroundcolor='rgb(230, 230,230)'
#        ),
#        zaxis=dict(
#            gridcolor='rgb(255, 255, 255)',
#            zerolinecolor='rgb(255, 255, 255)',
#            showbackground=True,
#            backgroundcolor='rgb(230, 230,230)'
#        )
#    )
)

fig = go.Figure(data=traces,layout=layout)
plotly.offline.plot(fig,filename='Wrinkled_cylinder_slices.html')