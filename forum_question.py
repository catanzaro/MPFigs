# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:17:55 2018

@author: mikec
"""

import plotly
import plotly.graph_objs as go
import numpy as np

theta = np.linspace(0,2*np.pi,50) 
x = np.linspace(0,10,50) 
zthresh=2
sthrow=[]
dxthrow=[]


tg,xg = np.meshgrid(theta,x) 
y = np.zeros((50,50))
z = np.zeros((50,50))

for dx in range(50):
    for s in range(50):
        if 2*np.sin(theta[s]) <= zthresh:
            y[dx,s] = 2*np.cos(theta[s])
            z[dx,s] = 2*np.sin(theta[s])
        else:
            y[dx,s] = 2*np.cos(theta[s])
            z[dx,s] = np.nan
            

contours = dict(
        x=dict(
                highlight=True,
                project=dict(
                        x=True,
                        y=True,
                        z=True)),
        y=dict(
                highlight=False,
                project=dict(
                        x=True,
                        y=True,
                        z=True)),
        z=dict(
                highlight=True,
                project=dict(
                        x=True,
                        y=True,
                        z=True))
        )

surf = go.Surface(x=xg,y=y,z=z,contours=contours,opacity=0.7,hoverinfo='none')
fig = go.Figure(data=[surf])
plotly.offline.plot(fig)