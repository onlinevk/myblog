from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm,Textarea,TextInput
from django import forms
from documents.models import *
# Create your models here.

class Information(models.Model):
	title=models.CharField(max_length=100)
	info=models.TextField(max_length=200)	
	rating=models.IntegerField(blank=True,null=True)
	like=models.IntegerField(blank=True,null=True)
	tag=models.CharField(max_length=50)
	date_modified = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return u'%s' %(self.title)
	def get_absolute_url(self):
		return reverse('info_edit',kwargs={'pk':self.pk})

class InformationForm(ModelForm):
        class Meta:
                model=Information
		search_fields = ('title',)
		ordering = ('date_modified',)
		
class Comment(models.Model):
        document =models.ForeignKey(Document)
	info =models.ForeignKey(Information)
	comment=models.TextField(max_length=200)
        rating=models.IntegerField(blank=True,null=True)
        like=models.IntegerField(blank=True,null=True)
        date_modified = models.DateTimeField(auto_now=True)
        def __unicode__(self):
                return u'%s' %(self.comment)
        def get_absolute_url(self):
                return reverse('comment_edit',kwargs={'pk':self.pk})

class CommentForm(ModelForm):
        class Meta:
                model=Comment

