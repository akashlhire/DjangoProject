from django.urls import path

from . import views

urlpatterns = [
    path("",views.links_view.as_view(),name = "study-page")
    
]

