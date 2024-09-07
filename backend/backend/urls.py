from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('charts.urls')), 
    path('', views.home), 
]
