#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:37 2018

@author: mike
"""
import plotly
import plotly.graph_objs as go
import numpy as np


xdiv=100
tdiv=50
### Make the rectangular grid, the surface of the dented cylinder
theta = np.linspace(0,2*np.pi,tdiv) 
x = np.linspace(0,10,xdiv) 
## Thresholding here:
zval = [-2,-0.5] ## max range [-2,2]
yval=[-2,2] ## max range [-2,2]
xval = [0,10] ## max range [0,10]

tg,xg = np.meshgrid(theta,x) # grided versions

z = np.full((xdiv,tdiv),np.nan)
y = 2*np.cos(tg)







for dx in range(xdiv): # iterating x-coordinates
    for s in range(tdiv): # iterating theta-coordinates
        if theta[s] < 3*np.pi/2.: # 3/4 of the cylinder is perfect
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

#zmax = np.nanmax(z)
#for dx in range(xdiv-1):
#    for s in range(tdiv-1):
#        if not np.isnan(z[dx,s]):
#            if np.isnan(z[dx+1,s]) or np.isnan(z[dx-1,s]) or np.isnan(z[dx,s+1]) or np.isnan(z[dx,s-1]):
#                z[dx,s] = zmax
#                print('change!')




contours = dict(
        x=dict(
                show=False,
                highlight=True,
                highlightcolor='black',
                highlightwidth=10,
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
                highlight=False,
                usecolormap=True,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        )
s1 = go.Surface(x=xg,y=y,z=z,opacity=0.7,colorscale='deep',contours=contours,showscale=False,hoverinfo='none')


#
#
#### Set the layout params
#
layout = go.Layout(
    title='Wrinkled cylinder with z-range = {}, y-range = {}, and x-range = {}'.format(zval, yval,xval),
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

fig = go.Figure(data=[s1], layout=layout)
#py.plot(fig, filename='Wrinkled_cylinder')
plotly.offline.plot(fig,filename='Wrinkled_cylinder.html')