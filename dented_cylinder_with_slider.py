#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:37 2018

@author: mike
"""
import plotly
import plotly.graph_objs as go
import numpy as np
import dash 
import dash_core_components as dcc
import dash_html_components as html
#import plotly.figure_factory as FF


### Make the caps of the (undented) cylinder
theta = np.linspace(0,2*np.pi,50) 
x = np.linspace(0,1,50) 
xx = np.linspace(9,10,50)

tg,xg = np.meshgrid(theta,x) # grided versions

y = 2*np.cos(tg)
z = 2*np.sin(tg)

s1 = go.Surface(x=xg,y=y,z=z)
s7 = go.Surface(x=np.meshgrid(theta,np.linspace(9,10,50))[1],y=y,z=z)

### Transition from circle to start of dent

x = np.linspace(1,3,50)
xg = np.meshgrid(theta,x)[1]
y = 2*np.cos(tg)
z = np.zeros((50,50))
for s in range(50): # Iterate over theta coordinates
    for dx in range(50): # Iterate over x coordinates
        if theta[s] < 3*np.pi/2.:
            z[dx,s] = 2*np.sin(theta[s])
        else:
            z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((x[dx]-1)/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(x[dx]-1)/2)
    #print(z)
s3 = go.Surface(x=xg,y=y,z=z)

# Wrinkle

x = np.linspace(3,5,50)
xg = np.meshgrid(theta,x)[1]
y = 2*np.cos(tg)
z = np.zeros((50,50))
for s in range(50): # Iterate over theta coordinates
    for dx in range(50): # Iterate over x coordinates
        if theta[s] < 3*np.pi/2.:
            z[dx,s] = 2*np.sin(theta[s])
        else:
            z[dx,s] = ((1/14.)+(6/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)-1
    #print(z)

s4 = go.Surface(x=xg,y=y,z=z)

# Wrinkle
x = np.linspace(5,7,50)
xg = np.meshgrid(theta,x)[1]
y = 2*np.cos(tg)
z = np.zeros((50,50))
for s in range(50): # Iterate over theta coordinates
    for dx in range(50): # Iterate over x coordinates
        if theta[s] < 3*np.pi/2.:
            z[dx,s] = 2*np.sin(theta[s])
        else:
            z[dx,s] = ((1/14.)+(6/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)-1
    #print(z)

s5 = go.Surface(x=xg,y=y,z=z)

x = np.linspace(7,9,50)
xg = np.meshgrid(theta,x)[1]
y = 2*np.cos(tg)
z = np.zeros((50,50))
for s in range(50): # Iterate over theta coordinates
    for dx in range(50): # Iterate over x coordinates
        if theta[s] < 3*np.pi/2.:
            z[dx,s] = 2*np.sin(theta[s])
        else:
            z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((9-x[dx])/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(9-x[dx])/2)
    #print(z)
s6 = go.Surface(x=xg,y=y,z=z)


### Set the layout params

layout = go.Layout(
    title='Dented Cylinder',
    xaxis=dict(
            rangeselector=dict(),
            rangeslider=dict(
                    autorange=True,
                    ),
            type="linear")
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

fig = go.Figure(data=[s1,s3,s4,s5,s6,s7], layout=layout)
#py.iplot(fig, filename='Parametric_plot')
plotly.offline.plot(fig,filename='Dented_cylinder_slider.html')