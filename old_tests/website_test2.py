# -*- coding: utf-8 -*-
"""
Created on Tue May 15 07:16:01 2018

@author: mikec
"""

import plotly.plotly as py
import ipywidgets as widgets

from ipywidgets import interact, interactive, fixed
from IPython.core.display import HTML
from IPython.display import display, clear_output
from plotly.widgets import GraphWidget


styles = '''<style>.widget-hslider { width: 100%; }
    .widget-hbox { width: 100% !important; }
    .widget-slider { width: 100% !important; }</style>'''

HTML(styles)

#this widget will display our plotly chart
graph = GraphWidget("https://plot.ly/~chriddyp/674")
fig = py.get_figure("https://plot.ly/~chriddyp/674")

#find the range of the slider.
xmin, xmax = fig['layout']['xaxis']['range']

# use the interact decorator to tie a widget to the listener function
@interact(y=widgets.FloatRangeSlider(min=xmin, max=xmax, step=(xmax-xmin)/1000.0, continuous_update=False))
def update_plot(y):
    graph.relayout({'xaxis.range[0]': y[0], 'xaxis.range[1]': y[1]})
    
#display the app    
graph