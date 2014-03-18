from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm,Textarea,TextInput
from django import forms

# Create your models here.


class UserType(models.Model):
	type_name=models.CharField(max_length=50)
	description=models.CharField(max_length=100)
	date_modified = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.type_name
class UserTypeForm(ModelForm):
        class Meta:
                model=UserType	
	

class User(models.Model):
        user_type =models.ForeignKey(UserType)
	user_name =models.CharField(max_length=50)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email_id=models.CharField(max_length=50)
	gender=models.CharField(max_length=10)
	qualification=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	city=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	country=models.CharField(max_length=10)
	date_modified = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.user_name
	def get_absolute_url(self):
		return reverse('info_edit',kwargs={'pk':self.pk})

class UserForm(ModelForm):
	def __init__(self, *args, **kwargs): 
        	super(ModelForm, self).__init__(*args, **kwargs)
        	self.css_class = "rule"

    	class Meta:
        	model = User
        	fields = ("user_name",)
        	widgets = {
            		"user_name" : TextInput(attrs={"class" : "title"}),
        		}
        	

class UserLoginAccount(models.Model):
        user_name=models.ForeignKey(User)
	password=models.CharField(max_length=100)
	date_modified = models.DateTimeField(auto_now=True)
class UserLoginAccountForm(ModelForm):
        class Meta:
                model=UserLoginAccount
