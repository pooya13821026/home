from django.contrib.auth import get_user, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from dashbord.forms import EditProfileForm, ChangePasswordForm
from estate.models import *


class Dashbord(TemplateView):
    template_name = 'dashbord/dashbord.html'


class EditProfile(View):
    def get(self, request: HttpRequest):
        user = get_user(request)
        form = EditProfileForm(instance=user)
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'dashbord/edit_profile.html', context)

    def post(self, request: HttpRequest):
        user = get_user(request)
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save(commit=True)
        context = {
            'form': form,
            'user': user
        }
        return render(request, 'dashbord/edit_profile.html', context)


def dashbord_component(request):
    return render(request, 'dashbord/component/dashbord_component.html')


class ChangePass(View):
    def get(self, request: HttpRequest):
        change_pass_form = ChangePasswordForm()
        context = {
            'change_pass_form': change_pass_form,
        }
        return render(request, 'dashbord/changepassword.html', context)

    def post(self, request: HttpRequest):
        change_pass_form = ChangePasswordForm(request.POST)
        if change_pass_form.is_valid():
            user = get_user(request)
            if user.check_password(change_pass_form.cleaned_data.get('current_password')):
                user.set_password(change_pass_form.cleaned_data.get('new_password'))
                user.save()
                logout(request)
                return redirect(reverse('home'))  # login
            else:
                change_pass_form.add_error('current_password', 'کلمه عبور وارد شده صحیح نیست')
        context = {
            'change_pass_form': change_pass_form,
        }
        return render(request, 'dashbord/changepassword.html', context)


class NewHome(View):
    def get(self, request):
        property_type = PropertyType.objects.all()
        category = Category.objects.all()
        state = State.objects.all()
        welfare_amenities = WelfareAmenities.objects.all()
        context = {
            'property_type': property_type,
            'category': category,
            'state': state,
            'welfare_amenities': welfare_amenities,
        }
        return render(request, 'dashbord/new_home.html', context)

    def post(self, request):
        pass
