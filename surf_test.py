#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:37 2018

@author: mike
"""
import plotly
import plotly.graph_objs as go
import numpy as np

x = []
y = []
z=[]

for i in range(101):
        x.append(2*np.cos(np.pi/50*i))
        y.append(2*np.sin(np.pi/50*i))
        z.append(0)
    
trace1 = go.Mesh3d(x=x,y=y,z=z)
trace2 = go.Mesh3d(x=x,y=y,z=[1 for i in range(101)])

plotly.offline.plot([trace1,trace2])