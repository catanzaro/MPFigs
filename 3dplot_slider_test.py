#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:04:02 2018

@author: mike
"""

import plotly.plotly as py
import ipywidgets as widgets
import numpy as np

from ipywidgets import interact, interactive, fixed
from IPython.core.display import HTML
from IPython.display import display, clear_output
from plotly.widgets import GraphWidget

g = GraphWidget('https://plot.ly/~DemoAccount/10147/')
x = y = np.arange(-5,5,0.1)
yt = x[:,np.newaxis]

# define our listener class
class z_data:
    
    def __init__(self):
        self.z = np.cos(x*yt)+np.sin(x*yt)*2
    
    def on_z_change(self, name):
        new_value = name['new']
        
        self.z = np.cos(x*yt*(new_value+1)/100)+np.sin(x*yt*(new_value+1/100))
        self.replot()
        
    def replot(self):
        g.restyle({ 'z': [self.z], 'colorscale': 'Viridis'})

# create sliders
z_slider = widgets.FloatSlider(min=0,max=30,value=1,step=0.05, continuous_update=False)
z_slider.description = 'Frequency'
z_slider.value = 1

# initialize listener class
z_state = z_data()

# activate listener on our slider
z_slider.observe(z_state.on_z_change, 'value')

# display our app
display(z_slider)
display(g)