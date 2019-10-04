"""fourthproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#1st way
# from django.contrib import admin
# from django.urls import path
# from greetingapp.views import greetings_views
# from timeapp.views import time_info_view
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('greetings/',greetings_views),
#     path('time/',time_info_view),
# ]


#2nd way
#this method is called alliasing
from django.contrib import admin
from django.urls import path
from greetingapp import views as v1
from timeapp import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings/',v1.greetings_views),
    path('time/',v2.time_info_view),
]
