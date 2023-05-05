from django.urls import path

from . import views

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<int:_id>/', views.author_about, name='author_about'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),

]
