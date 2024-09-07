from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def candlestick_data(request):
    data = {"data": [{"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35}]}
    return Response(data)

@api_view(['GET'])
def line_chart_data(request):
    data = {"labels": ["Jan", "Feb", "Mar"], "data": [10, 20, 30]}
    return Response(data)

@api_view(['GET'])
def bar_chart_data(request):
    data = {"labels": ["Product A", "Product B"], "data": [100, 150]}
    return Response(data)

@api_view(['GET'])
def pie_chart_data(request):
    data = {"labels": ["Red", "Blue"], "data": [300, 50]}
    return Response(data)
