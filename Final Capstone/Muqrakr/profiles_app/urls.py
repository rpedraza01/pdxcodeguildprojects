from django.urls import path

from . import views

app_name = 'profiles_app'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('intro/', views.IntroToCFView.as_view(), name='intro_to_cf'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/api/', views.api, name='api'),
    path('your_profile/', views.YourProfileView.as_view(), name='your_profile'),
    path('update_your_profile/', views.UpdateYourProfile.as_view(), name='update_your_profile'),
    path('create_your_profile/', views.CreateYourProfile.as_view(), name='create_your_profile'),
    path('ajax/save_search/', views.ajax_save_search, name='save_search'),
    path('ajax/save_search_committee/', views.ajax_save_search_committee, name='save_search_committee'),
    path('candidate_csv/',views.save_search_csv, name='candidate_csv'),
    path('committee_csv/', views.save_search_committee_csv, name='committee_csv'),
    path('delete_candidate/', views.delete_candidate, name='delete_candidate'),
    path('delete_committee/', views.delete_committee, name='delete_committee'),
]