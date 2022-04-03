from django.urls import path

from . import views

urlpatterns = [
    path("",views.firstapp, name="home-page"),
    path("about",views.about_us, name="about-page"),
    path("courses",views.courses, name="courses-page"),
    path("fees",views.fees, name="fees-page"),
    path("test",views.test_series, name="test-series-page" )
]


