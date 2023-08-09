from django import forms
from estate.models import SendVisit, Estate


class SearchForm(forms.Form):
    search = forms.CharField()


class SendVisitForm(forms.ModelForm):
    class Meta:
        model = SendVisit
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'نام و نام خانوادگی',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل',
                'class': 'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'placeholder': 'موبایل',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'متن پیام',
                'class': 'form-control',
                'rows': 4
            }),
        }


class FilterForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ['state']

class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = ['title', 'address', 'meterage', 'description', "price"]
