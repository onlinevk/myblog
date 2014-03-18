from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm,Textarea,TextInput
from django import forms
from information.models import *
# Create your models here.
class DocumentCategory(models.Model):
	category_name=models.CharField(max_length=50)
	description=models.CharField(max_length=100)
	date_modified = models.DateTimeField(auto_now=True)

class DocumentCategoryForm(ModelForm):
        class Meta:
                model=DocumentCategory

class Document(models.Model):
        category =models.ForeignKey(DocumentCategory)
        #comment =models.ForeignKey(Comment)
	title=models.CharField(max_length=100)
	short_description=models.TextField(max_length=200)	
	description=models.TextField(max_length=200)	
	submited_by=models.IntegerField(blank=True,null=True)
	date_modified = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return u'%s' %(self.title)
	def get_absolute_url(self):
		return reverse('doc_edit',kwargs={'pk':self.pk})

class DocumentForm(ModelForm):
        class Meta:
                model=Document
		search_fields = ('title',)
		ordering = ('date_modified',)
	

