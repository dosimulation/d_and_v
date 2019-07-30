from django.shortcuts import render, redirect
from .models import *
from django.core.files.base import ContentFile
# for plotting
import plotly.offline as opy
import plotly.graph_objs as go


# main page
def index(request):
    return render(request, 'index.html')

# taking the translog data table, returns the total number
# of observations back to the transportation html page

# https://stackoverflow.com/questions/5631247/displaying-graphs-charts-in-django
def transportation(request):

    Nrows = TransLog.objects.count()

    x = [-2,0,4,6,7]
    y = [q**2-q+3 for q in x]
    trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                        mode="lines",  name='1st Trace')

    data=go.Data([trace1])
    layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
    figure=go.Figure(data=data,layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    context = {
        'nobs' : Nrows,
        'graph': div,
              }
    return render(request, 'transportation.html', context)

def diabetes(request):
    return render(request, 'diabetes.html')

def nutrition(request):
    return render(request, 'nutrition.html')
