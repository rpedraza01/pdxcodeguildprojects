from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import YourProfile

class HomePageView(TemplateView):
    success_url = reverse_lazy('home')
    template_name = 'home.html'

class AboutView(TemplateView):
    # success_url = reverse_lazy('about')
    template_name = 'about.html'

class IntroToCFView(TemplateView):
    # success_url = reverse_lazy('intro_to_cf')
    template_name = 'intro_to_cf.html'

class SearchView(TemplateView):
    # success_url = reverse_lazy('search')
    template_name = 'search.html'

class YourProfileView(LoginRequiredMixin, TemplateView):
    # success_url = reverse_lazy('your_profile')
    template_name = 'your_profile.html'

class CreateYourProfile(LoginRequiredMixin, CreateView):
    model = YourProfile
    template_name = 'create_your_profile.html'
    fields = ['user_title', 'about_user', 'user_pic']
    login_url = 'login'
    success_url = reverse_lazy('your_profile.html')

    def form_valid(self, form):
        form.instance.user_name = self.request.users_app.CustomUser
        return super().form_valid(form)

class UpdateYourProfile(LoginRequiredMixin, UpdateView):
    model = YourProfile
    template_name = 'update_your_profile.html'
    fields = ['user_title', 'about_user', 'user_pic']
    success_url = reverse_lazy('your_profile.html')