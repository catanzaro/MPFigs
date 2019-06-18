# -*- coding: utf-8 -*-
"""
Created on Sat May 19 15:15:40 2018

@author: mikec
"""

import plotly.plotly as py
import ipywidgets as widgets

from ipywidgets import interact, interactive, fixed
from IPython.core.display import HTML
from IPython.display import display, clear_output
from plotly.widgets import GraphWidget
from traitlets import link


styles = '''<style>.widget-hslider { width: 100%; }
    .widget-hbox { width: 100% !important; }
    .widget-slider { width: 100% !important; }</style>'''

HTML(styles)

#this widget will display our plotly chart
graph = GraphWidget("https://plot.ly/~chriddyp/674")
fig = py.get_figure("https://plot.ly/~chriddyp/674")

#find the range of the slider.
xmin, xmax = fig['layout']['xaxis']['range']

# let's define our listener functions that will respond to changes in the sliders
def on_value_change_left(change):
    graph.relayout({'xaxis.range[0]': change['new']})
    
def on_value_change_right(change):
    graph.relayout({'xaxis.range[1]': change['new']})
    
# define the sliders
left_slider = widgets.FloatSlider(min=xmin, max=xmax, value=xmin, description="Left Slider")
right_slider = widgets.FloatSlider(min=xmin, max=xmax, value=xmax, description="Right Slider")

# put listeners on slider activity
left_slider.observe(on_value_change_left, names='value')
right_slider.observe(on_value_change_right, names='value')

# set a relationship between the left and right slider
link((left_slider, 'max'), (right_slider, 'value'))
link((left_slider, 'value'), (right_slider, 'min'))

# display our app
display(left_slider)
display(right_slider)
display(graph)