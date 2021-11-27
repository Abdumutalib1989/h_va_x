from django.urls import path
from django.contrib import admin
from qidiruv.views import index, natija



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('search', natija),



]
