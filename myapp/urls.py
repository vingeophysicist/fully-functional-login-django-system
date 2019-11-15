"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from core.views import QuizDetailView
from core import views
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name= 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('secret/', views.secret_page, name= 'secret'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url(r'^(?P<slug>[\w-]+)/', view=QuizDetailView.as_view(), name='quizview')
]
