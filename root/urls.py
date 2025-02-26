from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('/gituser',views.handleGit,name='gituser'),
    path('/repos/',views.repos,name='repos'),
]
