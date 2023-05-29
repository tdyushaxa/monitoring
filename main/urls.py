from django.urls import path
from .import views


app_name = 'main'

urlpatterns = [
    path('', views.ComputerPageView, name='computer'),
    path('hafta', views.ComputerHaftaPageView, name='computer__hafta'),
    path('printer/', views.PrinterPageView, name='printer'),
    path('printer/hafta/', views.PrinterHaftaPageView, name='printer__hafta'),
    path('proektor/', views.ProektorPageView, name='proektor'),
    path('proektor/hafta', views.ProyektorHaftaPageView, name='proektor'),
    path('wifi/', views.WifiPageView, name='wifi'),
    path('wifi/hafta', views.WifiHaftaPageView, name='wifi__hafta'),
    path('camera/', views.CameraPageView, name='camera'),
    path('camera/hafta', views.CameraHaftaPageView, name='camera'),
    path('update/',views.UPdateView,name='update')

]
