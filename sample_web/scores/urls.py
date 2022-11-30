from django.urls import path, re_path

from . import views

app_name = 'scores'
urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^scores/', views.get_score, name='view_score'),
    re_path(r'^scores/(?P<user_input>[0-9]{1,2})', views.get_score, name='get_score'),

]
