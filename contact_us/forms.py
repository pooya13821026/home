from django import forms

from contact_us.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'mobile', 'message']
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
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'mobile': 'موبایل',
            'message': 'متن پیام',
        }
        error_messages = {
            'full_name': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'email': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'mobile': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'message': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
        }
