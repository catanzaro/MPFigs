#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:37 2018

@author: mike
"""
import plotly
import plotly.graph_objs as go
import numpy as np
import cmocean
import dash_core_components as dcc
import dash_html_components as html
#import plotly.figure_factory as FF

xdiv=100
tdiv=50
### Make the rectangular grid, the surface of the dented cylinder
theta = np.linspace(0,2*np.pi,tdiv) 
x = np.linspace(0,10,xdiv) 
#zthresh = np.cos(theta[25])
zval=[-2,2]
xval=[0,10]


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


contours = dict(
        x=dict(
                show=False,
                highlight=True,
                highlightwidth=15,
                usecolormap=False,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        y=dict(
                show=False,
                highlight=False,
                usecolormap=False,
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
s1 = go.Surface(x=xg,y=y,z=z,opacity=0.7,surfacecolor='cmocean',hoverinfo='none',contours=contours,showscale=False)



#s1 = go.Surface(x=xg,y=y,z=z)
#s7 = go.Surface(x=np.meshgrid(theta,np.linspace(9,10,50))[1],y=y,z=z)
#
#### Transition from circle to start of dent
#
#x = np.linspace(1,3,50)
#xg = np.meshgrid(theta,x)[1]
#y = 2*np.cos(tg)
#z = np.zeros((50,50))
#for s in range(50): # Iterate over theta coordinates
#    for dx in range(50): # Iterate over x coordinates
#        if theta[s] < 3*np.pi/2.:
#            z[dx,s] = 2*np.sin(theta[s])
#        else:
#            z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((x[dx]-1)/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(x[dx]-1)/2)
#    #print(z)
#s3 = go.Surface(x=xg,y=y,z=z)
#
## Wrinkle
#
#x = np.linspace(3,5,50)
#xg = np.meshgrid(theta,x)[1]
#y = 2*np.cos(tg)
#z = np.zeros((50,50))
#for s in range(50): # Iterate over theta coordinates
#    for dx in range(50): # Iterate over x coordinates
#        if theta[s] < 3*np.pi/2.:
#            z[dx,s] = 2*np.sin(theta[s])
#        else:
#            z[dx,s] = ((1/14.)+(6/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)-1
#    #print(z)
#
#s4 = go.Surface(x=xg,y=y,z=z)
#
## Wrinkle
#x = np.linspace(5,7,50)
#xg = np.meshgrid(theta,x)[1]
#y = 2*np.cos(tg)
#z = np.zeros((50,50))
#for s in range(50): # Iterate over theta coordinates
#    for dx in range(50): # Iterate over x coordinates
#        if theta[s] < 3*np.pi/2.:
#            z[dx,s] = 2*np.sin(theta[s])
#        else:
#            z[dx,s] = ((1/14.)+(6/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)-1
#    #print(z)
#
#s5 = go.Surface(x=xg,y=y,z=z)
#
#x = np.linspace(7,9,50)
#xg = np.meshgrid(theta,x)[1]
#y = 2*np.cos(tg)
#z = np.zeros((50,50))
#for s in range(50): # Iterate over theta coordinates
#    for dx in range(50): # Iterate over x coordinates
#        if theta[s] < 3*np.pi/2.:
#            z[dx,s] = 2*np.sin(theta[s])
#        else:
#            z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((9-x[dx])/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(9-x[dx])/2)
#    #print(z)
#s6 = go.Surface(x=xg,y=y,z=z)
#
#
#### Set the layout params
#
steps = list()
for step in range(500):
    steps.append(dict(
            args=[{}],
            value=step,
            
            ))
layout = go.Layout(
    title='Dented Cylinder with Threshold',
    showlegend=False,
    scene= dict(
        zaxis=dict(
            showspikes=False,
            range=zval),
        xaxis=dict(
            showspikes=False,
            range=xval),
        yaxis=dict(
            showspikes=False)
    ),
    sliders=[dict(
            visible=True,
            steps=[dict(
                    args=
                    method='relayout'))]
)

fig = go.Figure(data=[s1], layout=layout)
#py.iplot(fig, filename='Parametric_plot')
plotly.offline.plot(fig,filename='Dented_cylinder_slider.html')