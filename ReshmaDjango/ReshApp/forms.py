from django import forms

# Create your models here.

from django.utils import timezone
from ReshApp.models import Student

class Emp(forms.Form):
       eid = forms.CharField(max_length=10)
       ename=forms.CharField(max_length=24)
       eadd = forms.CharField(max_length=40)
       dob = forms.DateTimeField()

class studentmodelform(forms.ModelForm):
	class Meta:
		model = Student
		fields=('sid' , 'sname')

       
