from django.urls import path
from . import views
app_name = 'test_me'
urlpatterns = [
    path('', views.inputnum, name='inputnum'),
    #path('<int:id>/', views.multi, name='multi'),
    #path('<int:id>/', views.multiplication, name='multipi'),
    path('multipli/', views.multiplication, name='multipli'),
    path('inputnum/', views.inputnum, name='inputnum')
]