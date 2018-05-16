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

xdiv=100
tdiv=60
### Make the rectangular grid, the surface of the dented cylinder
theta = np.linspace(0,2*np.pi,tdiv) 
x = np.linspace(0,10,xdiv) 
#zthresh = np.cos(theta[25])
zthresh = -1

tg,xg = np.meshgrid(theta,x) # grided versions

z = np.full((xdiv,tdiv),np.nan)
y = 2*np.cos(tg)







for dx in range(xdiv): # iterating x-coordinates
    for s in range(tdiv): # iterating theta-coordinates
        if theta[s] < 3*np.pi/2.: # 3/4 of the cylinder is perfect
           if 2*np.sin(theta[s]) <= zthresh: #check
               z[dx,s] = 2*np.sin(theta[s])
        elif x[dx] <= 1 or x[dx] >= 9: #make the caps of the cylinder
            if 2*np.sin(theta[s]) <= zthresh:
                 z[dx,s] = 2*np.sin(theta[s])
        elif 1<x[dx]<=3: # begin the deformation
            if ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((x[dx]-1)/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(x[dx]-1)/2) <= zthresh:    
                z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((x[dx]-1)/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(x[dx]-1)/2)
        elif 3<x[dx]<=5: # wrinkle   
            if ((1/14.)+(6/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)-1 <= zthresh:
                z[dx,s] = ((1/14.)+(6/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((x[dx]-3)/2))*(4*np.cos(theta[s])-2)-1
        elif 5<x[dx]<=7: # wrinkle
            if ((1/14.)+(6/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)-1 <= zthresh:
                z[dx,s] = ((1/14.)+(6/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)**3 + (3/14. -(24/14.)*((7-x[dx])/2))*(4*np.cos(theta[s])-2)-1
        elif 7<x[dx]<=9: # end the dent
            if ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((9-x[dx])/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(9-x[dx])/2) <= zthresh:
                z[dx,s] = ((4./7)*(2*np.cos(theta[s])-1)**3 + (3./7)*(2*np.cos(theta[s])-1)-1)*((9-x[dx])/2)+ (-1)*(np.sqrt(4-(2*np.cos(theta[s]))**2))*(1-(9-x[dx])/2)


contours = dict(
        x=dict(
                show=True,
                highlight=True,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        y=dict(
                show=True,
                highlight=True,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        z=dict(
                show=True,
                highlight=True,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        )
s1 = go.Surface(x=xg,y=y,z=z,opacity=0.7,surfacecolor='cmocean',hoverinfo='none')



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
layout = go.Layout(
    title='Dented Cylinder with Threshold '+str(zthresh),
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

fig = go.Figure(data=[s1], layout=layout)
#py.iplot(fig, filename='Parametric_plot')
plotly.offline.plot(fig,filename='Dented_cylinder_slider.html')