"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from questionbox import views as question_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',question_views.home, name='home'),
    path('question/add/', question_views.add_question, name='add_question'),
    path('questions/list/', question_views.list_questions, name='list_questions'),

    #path('questionbox/', include('questionbox.urls')),
    #path('', views.index, name='index'),
    #path('questions/add/', question_views.add_question, name='add_question'),
    #path('questions/<int:pk>/add_answer', question_views.add_answer, name='add_answer'),
    #path('question/<int:pk>/star', question_views.star_question, name='star_question'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        #For django versions before 2.0:
        #url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
