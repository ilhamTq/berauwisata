from django.shortcuts import render, redirect
from re import template
from django.urls import path, include
# from .models import Artikel, Kategori
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Biodata

from .forms import UserForms, BiodataForms
# from .models import User, Group

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
@user_passes_test(is_operator)
def users(request):
    template_name = "back/users/table_user.html"
    list_user = User.objects.all()
    context = {
        'title':'Tabel User',
        'list_user':list_user
    }
    
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_detil(request, id):
    template_name = "back/users/user_detil.html"
    try:
        user_info = User.objects.get(id=id)
        biodataku = Biodata.objects.get(user=user_info)
    except:
        return redirect(users)
    context = {
        'title':'Detail User',
        'user_info':user_info,
        'biodataku':biodataku,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_edit(request, id):
    template_name = "back/users/user_edit.html"   
    try:
        user_info = User.objects.get(id=id)
        biodataku = Biodata.objects.get(user=user_info)
    except:
        return redirect(users)
    if request.method == "POST":
        form_user = UserForms(request.POST, instance=user_info)
        form_biodata = BiodataForms(request.POST, instance=biodataku)
        if form_user.is_valid() and form_biodata.is_valid():
            test = form_user.save(commit=False)
            test.is_active = True
            test.save()
            form_biodata.save()
            return redirect(users)
    else:
        form_user = UserForms(instance=user_info)
        form_biodata = BiodataForms(instance=biodataku)
    context = {
        'title':'Edit User',
        'user_info':user_info,
        'biodataku':biodataku,
        
        'form_user':form_user,
        'form_biodata':form_biodata,
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_delete(request, id):
    try:
        User.objects.get(id=id).delete()
    except:
        pass
    return redirect(users)