from django.forms import ModelForm
from petition.models import *
from django import forms

        
class Form(ModelForm):
    contents = forms.CharField(widget = forms.Textarea(attrs={'style' : "width:1000px; height:500px;", 'class' : "content" , 'name' : "content" }))
    counter = forms.IntegerField(widget = forms.NumberInput(attrs={'id' : 'count',  'type':'hidden'}))
    title = forms.CharField(widget = forms.Textarea(attrs={'class' : 'title_form'}))
    
    class Meta:
        model = Article
        fields=['name', 'title','contents','url','email','counter']