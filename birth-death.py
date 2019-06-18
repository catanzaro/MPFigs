# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:12:23 2018

@author: mikec
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
#theta = np.linspace(0,2*np.pi,tdiv) 
x = np.linspace(-3,3,xdiv) 
xg,yg = np.meshgrid(x,x)
#zthresh = np.cos(theta[25])


z = xg**3 + 3*xg*(yg**2-1)

contours = dict(
        x=dict(
                show=False,
                highlight=False,
                highlightwidth=15,
                usecolormap=False,
                project=dict(
                        x=False,
                        y=False,
                        z=False)),
        y=dict(
                show=False,
                highlight=True,
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

s1 = go.Surface(x=xg,y=yg,z=z,opacity=0.7,surfacecolor='cmocean',contours=contours,showscale=False,hoverinfo='none')


#
#
#### Set the layout params
#
layout = go.Layout(
    title='x^3+tx',
    scene=dict(
        #aspectratio=dict(
        #    x=1.84296,y=0.73642,z=0.73680),
        zaxis = dict(
            showspikes=False,
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            title=''),
            #range=zval),
        xaxis = dict(
                showspikes=False,
                #range=xval,
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                ticks='',
                title = 't-axis',
                showline=False),
        yaxis=dict(
                range=[-4,4],
                showgrid=False,
                zeroline=False,
                showticklabels=False,
                showspikes=False,
                ticks='',
                showline=False,
                title='')
        )
)

fig = go.Figure(data=[s1], layout=layout)
#py.iplot(fig, filename='Parametric_plot')
plotly.offline.plot(fig,filename='Dented_cylinder.html')