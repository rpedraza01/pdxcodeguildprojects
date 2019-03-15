from django.urls import path

from . import views

app_name = 'profiles_app'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('intro/', views.IntroToCFView.as_view(), name='intro_to_cf'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('your_profile/', views.YourProfileView.as_view(), name='your_profile'),
    path('update_your_profile/', views.UpdateYourProfile.as_view(), name='update_your_profile'),
    path('create_your_profile/', views.CreateYourProfile.as_view(), name='create_your_profile'),
]