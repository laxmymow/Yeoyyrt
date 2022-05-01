from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/newpost/',views.new_user_post, name="new_user_post")
]
