from django.urls import path

from account import views

app_name = 'account'
urlpatterns = [
    path('login/',views.LoginPageView,name='login'),
    path('logut/',views.LogoutPageView,name='logout'),

]
