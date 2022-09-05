from django import forms
from listatech.models import Post

class Postlink(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"