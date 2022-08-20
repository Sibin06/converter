from django.contrib import admin


from django.urls import path
from number import views



urlpatterns=[

    path("conv",views.NumWordView.as_view(),name='changer')

]