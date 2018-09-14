''' Present an interactive function explorer with slider widgets.

Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.

Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve sliders.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/sliders

in your browser.

'''
import numpy as np
import pandas as pd

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

# Set up data
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))


# Set up plot
# plot = figure(plot_height=400, plot_width=400, title="my sine wave",
#              tools="crosshair,pan,reset,save,wheel_zoom",
#              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

# plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

### plot 2
archivo = pd.read_csv("../data/datos_equipos.csv", sep="|") 
equipos = ['CLUB SPORT EMELEC', 'EL NACIONAL','DEPORTIVO CUENCA','INDEPENDIENTE DEL VALLE','BARCELONA SPORTING CLUB','SOCIEDAD DEPORTIVO AUCAS','DELFIN SPORTING CLUB',
'LIGA DEPORTIVA UNIVERSITARIA DE QUITO','MACARA DE AMBATO','TECNICO UNIVERSITARIO','GUAYAQUIL CITY FUTBOL CLUB','UNIVERSIDAD CATOLICA']
campeonatos = archivo['Campeonatos']

source = ColumnDataSource(data=dict(equipos=equipos, counts=campeonatos))

plot = figure(x_range=equipos, plot_height=350, toolbar_location=None, 
        tools="crosshair,pan,reset,save,wheel_zoom",
        title="CAMPEONATOS")
plot.vbar(x='equipos', top='counts', width=0.9, source=source, legend="equipos",
       line_color='white', fill_color=factor_cmap('equipos', palette=Spectral6, factors=equipos))

plot.xgrid.grid_line_color = None
plot.y_range.start = 0
plot.y_range.end = 30
plot.legend.orientation = "horizontal"
plot.legend.location = "top_center"



# Set up widgets
text = TextInput(title="title", value=u'CAMPEONATOS DEL ECUADOR')
v1 = Slider(title="CLUB SPORT EMELEC", value=0.0, start=0.0, end=15.0, step=1)
v2 = Slider(title="EL NACIONAL", value=0.0, start= 0.0, end=15.0, step=1)
v3 = Slider(title="DEPORTIVO CUENCA", value=0.0, start=0.0, end=15.0, step=1)
v4 = Slider(title="INDEPENDIENTE DEL VALLE", value=0.0, start=0.0, end=15.0, step=1)
v5 = Slider(title="BARCELONA SPORTING CLUB", value=0.0, start=0.0, end=15.0, step=1)
v6 = Slider(title="SOCIEDAD DEPORTIVA AUCAS", value=0.0, start=0.0, end=15.0, step=1)
v7 = Slider(title="DELFIN SPORTING CLUB", value=0.0, start=0.0, end=15.0, step=1)
v8 = Slider(title="LIGA DEPORTIVA UNIVERSITARIA DE QUITO", value=0.0, start= 0.0, end=15.0, step=1)
v9 = Slider(title="MACARA DE AMBATO", value=0.0, start=0.0, end=15.0, step=1)
v10 = Slider(title="TECNICO UNIVERSITARIO", value=0.0, start=0.0, end=15.0, step=1)
v11 = Slider(title="GUAYAQUIL CITY FUTBOL CLUB", value=0.0, start=0.0, end=15.0, step=1)
v12 = Slider(title="UNIVERSIDAD CATOLICA", value=0.0, start=0.0, end=15.0, step=1)

# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    a = v1.value
    b = v2.value
    c = v3.value
    d = v4.value
    e = v5.value
    f = v6.value
    g = v7.value
    h = v8.value
    i = v9.value
    j = v10.value
    k = v11.value
    l = v12.value


    # Generate the new curve
    #x = np.linspace(0, 4*np.pi, N)
    #y = a*np.sin(k*x + w) + b
    
    equipos = ['CLUB SPORT EMELEC', 'EL NACIONAL','DEPORTIVO CUENCA','INDEPENDIENTE DEL VALLE','BARCELONA SPORTING CLUB','SOCIEDAD DEPORTIVO AUCAS','DELFIN SPORTING CLUB',
    'LIGA DEPORTIVA UNIVERSITARIA DE QUITO','MACARA DE AMBATO','TECNICO UNIVERSITARIO','GUAYAQUIL CITY FUTBOL CLUB','UNIVERSIDAD CATOLICA']
    campeonatos = [a, b, c, d, e, f, g, h, i, j, k ,l]
    source.data = dict(equipos=equipos, counts=campeonatos)

for w in [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(text, v1, v2, v3, v4, v5, v6, v7,v8, v9, v10, v11, v12)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"
