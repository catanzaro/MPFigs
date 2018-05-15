#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:37 2018

@author: mike
"""
import plotly
import plotly.graph_objs as go
import numpy as np
#import plotly.figure_factory as FF


### The following works great for the cylinder
t = np.linspace(0,2*np.pi,50)
x = np.linspace(0,2,50)

tg,xg = np.meshgrid(t,x)

y = 2*np.cos(tg)
z = 2*np.sin(tg)


#x = np.linspace(-1,1,50)
#y = np.linspace(-2,2,50)
#
#xg,yg = np.meshgrid(x,y)
#
#z = yg**3 - xg*yg


surf = go.Surface(x=xg,y=y,z=z)

layout = go.Layout(
    title='Parametric Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    )
)

fig = go.Figure(data=[surf], layout=layout)
#py.iplot(fig, filename='Parametric_plot')
plotly.offline.plot(fig)