from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import datetime
import plotly
import sys


# def index(request):
#     fig = get_graph()
#     graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")
#     context = {'meme': graph_div}
#     template = loader.get_template('SIRModel/index.html')
#     return HttpResponse(template.render(context, request))


def index(request):
    fig = plotly.graph_objects.Figure(
        data=[plotly.graph_objects.Bar(y=[2, 1, 3])],
        layout_title_text="A Figure Displayed with fig.show()"
    )
    graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")
    context = {'meme': graph_div}
    template = loader.get_template('SIRModel/index.html')
    return HttpResponse(template.render(context, request))


def image(request):
    return HttpResponse("<img href='https://raw.githubusercontent.com/Ollie-spoon/legendary-octo-chainsaw/3fd9dd4accfb18e3593e9b8db35304bce0c0d81f/SIR_L.svg?token=AQMQURHS6H22FKKLNR3FXXDAOHQEQ'>")

