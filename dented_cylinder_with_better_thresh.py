#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:37 2018

@author: mike
"""
import plotly
import plotly.graph_objs as go
import numpy as np
#import dash 
#import dash_core_components as dcc
#import dash_html_components as html
#import plotly.figure_factory as FF

xdiv=100
tdiv=50
### Make the rectangular grid, the surface of the dented cylinder
theta = np.linspace(0,2*np.pi,tdiv) 
x = np.linspace(0,10,xdiv) 
#zthresh = np.cos(theta[25])
zthresh = 2.5
zmax=-0.5

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
s1 = go.Surface(x=xg,y=y,z=z,opacity=0.7,surfacecolor='cmocean',contours=contours)


#
#
#### Set the layout params
#
layout = go.Layout(
    title='Dented Cylinder with Threshold',
    scene=dict(
        #aspectratio=dict(
        #    x=1.84296,y=0.73642,z=0.73680),
        zaxis = dict(
            range=[-2.5,-0.5]),
        #xaxis = dict(
        #        range=[3,5])
            ),
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