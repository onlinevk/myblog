from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView, ListView, DetailView
from users.models import *
from django.core.urlresolvers import reverse_lazy

class ProfileList(ListView):
	model=User	
	

class ProfileCreate(CreateView):
	model=User
	success_url=reverse_lazy('user_list')

class ProfileUpdate(UpdateView):
	model=User
        success_url=reverse_lazy('user_list')

class ProfileDelete(DeleteView):
	model=User
        success_url=reverse_lazy('user_list')


