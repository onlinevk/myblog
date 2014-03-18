# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView,DeleteView, ListView, DetailView
from information.models import *
from django.core.urlresolvers import reverse_lazy

class InformationList(ListView):
	model=Information	
	

class InformationCreate(CreateView):
	model=Information
	success_url=reverse_lazy('information_list')

class InformationUpdate(UpdateView):
	model=Information
        success_url=reverse_lazy('information_list')

class InformationDelete(DeleteView):
	model=Information
        success_url=reverse_lazy('information_list')

class CommentList(ListView):
	model=Comment	

class CommentCreate(CreateView):
	model=Comment
	success_url=reverse_lazy('comment_list')


class CommentUpdate(UpdateView):
	model=Comment
        success_url=reverse_lazy('comment_list')

class CommentDelete(DeleteView):
	model=Comment
        success_url=reverse_lazy('comment_list')

def hitLike(request,pk):
	l=Information.objects.get(id=pk)
	if l.like==None:
		l.like=1
	else:
		l.like+=1
	Information.objects.filter(id=pk).update(like=l.like)
	obj=Information.objects.all()
	return render(request,'information/information_list.html',{'object_list':obj})
def aboutUs(request):
	return render(request,'staticpage/aboutus.html')	
def contactUs(request):
	return render(request,'staticpage/contactus.html')
def search(request):
	a=request.POST['title']
	if a==None:
		return HttpResponse(request,'None')
	else:	
		tiltes=Information.objects.filter(title__contains=a)[:5]
		return render(request,'information/search.html',{'titles':tiltes,'a':a})
def Info(request,pk):
	l=Information.objects.filter(id=pk)
	return render(request,'information/search_info_list.html',{'object_list':l})	

def preview(request):
	info=request.POST['info']
	title=request.POST['title']
	tag=request.POST['tag']
	return render(request,'information/preview.html',{'info':info,'title':title,'tag':tag})

