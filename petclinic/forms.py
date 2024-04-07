from django import forms
from .models import Owner
# class OwnerForm(forms.Form):
#     name = forms.CharField(label="name", max_length=50)
#     last_name = forms.CharField(label="last_name", max_length=50)
#     email = forms.EmailField(label="email", max_length=254)
#     phone = forms.CharField(label="phone", max_length=20)

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        #fields = ["name", "last_name", ]
        fields = "__all__"