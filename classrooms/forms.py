from django import forms
from classrooms.models import Category, secCategory


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=36, required=True)

    class Meta:
        model = Category
        fields = ['name'] 