from django.urls import path
from . import views
app_name = 'test_me'
urlpatterns = [
    #path('<int:id>/', views.multi, name='multi'), #3number
    #path('<int:id>/', views.multiplication, name='multipi'), #multiplication
    path('', views.inputnum, name='inputnum'),
    path('multipli/', views.multiplication, name='multipli'),
]