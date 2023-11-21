from django.urls import path
from appzz import views

urlpatterns = [
    path("hello", views.hello),
    path("done", views.done),
    path("ok", views.ok),
    path("showpage", views.showpage),
    path("dataform", views.dataform, name = 'dataform'),

    path('save-data', views.savedata),

    path('first', views.first),
    path('second', views.second),

]