from django import forms
from django.core.exceptions import ValidationError


from account.models import MyUser


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'mobile', 'email', 'addres', 'bio', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': '',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': '',
                'class': 'form-control'
            }),
            'mobile': forms.NumberInput(attrs={
                'placeholder': '',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': '',
                'class': 'form-control',
            }),
            'addres': forms.TextInput(attrs={
                'placeholder': '',
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'placeholder': '',
                'class': 'form-control',
                'rows': 3
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'mobile': 'موبایل',
            'avatar': 'عکس پروفایل',
            'bio': 'بیوگرافی',
            'addres': 'ادرس',
        }
        error_messages = {
            'first_name': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'last_name': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
            'mobile': {
                'required': 'پر کردن این قسمت الزامی میباشد'
            },
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    new_password = forms.CharField(
        label='کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور وارد شده با تکرار آن مطابقت ندارد')
