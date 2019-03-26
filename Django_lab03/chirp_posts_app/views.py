from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from .models import Post

class ChirpListView(ListView):
	model = Post
	template_name = 'chirp_posts_app/homepage.html'

	# def get_query_set(self):
	# 	return Post.objects.order_by('-date_edited')


class ChirpDetailView(LoginRequiredMixin, DetailView):
	model = Post
	template_name = 'chirp_posts_app/chirp_detail.html'


class ChirpCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'chirp_posts_app/chirp_new.html'
	fields = ['chirp_title', 'chirp_text']
	login_url = 'login'
	success_url = reverse_lazy('profiles:user_homepage')

	def form_valid(self, form):
		form.instance.chirp_author = self.request.user
		form.instance.author = self.request.user
		return super().form_valid(form)


class ChirpUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	template_name = 'chirp_posts_app/chirp_edit.html'
	fields = ['chirp_title', 'chirp_text']
	success_url = reverse_lazy('profiles:user_homepage')


class ChirpDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = 'chirp_posts_app/chirp_delete.html'
	success_url = reverse_lazy('profiles:user_homepage')


# class UserChirpListView(generic.ListView):
# 	model = Post
# 	template_name = 'chirp_posts_app/user_homepage.html'

	# def get_queryset(self):
	# 	# if self.chirp_author 
	# 	if self.request.user.is_authenticated:
	# 		return Post.objects.filter(chirp_author=self.request.user)
	# 	return Post.objects.all()


class UserListView(generic.ListView):
	model = User
	template_name = 'chirp_posts_app/user_list.html'