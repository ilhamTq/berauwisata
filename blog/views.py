from django.shortcuts import render, redirect
from django import forms
from re import template
from .models import Artikel, Kategori
from .forms import ArtikelForms
from django.contrib.auth.decorators import login_required, user_passes_test

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ArtikelSerializer

# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False
    

@login_required
# @user_passes_test(is_operator)
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
        print(request.session['is_operator'])
        
    template_name = "back/dashboard.html"
    context = {
        'title':'dashboard',
    }
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/artikel/table_artikel.html"
    artikel = Artikel.objects.filter(nama = request.user)

    context = {
        'title':'artikel',
        'artikel':artikel,
    }
    return render(request, template_name, context)

@login_required
def artikel_tambah(request):
    template_name = "back/artikel/artikel_tambah.html"
    kategori = Kategori.objects.all()  
    
    if request.method == "POST":
        forms_artikel = ArtikelForms(request.POST, request.FIlES)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            print(request.user)
            art.nama = request.user
            art.save()
            return redirect(artikel)
        
        # return redirect(artikel)
    else:
        forms_artikel = ArtikelForms()
    context = {
        'title':'Tambah Artikel',
        'kategori':kategori,
        'forms_artikel':forms_artikel,
    }
    return render(request, template_name, context)

@login_required
def view_artikel(request, id):
    template_name = "back/artikel/view_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title':'Detail Artikel',
        'artikel':artikel
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request, id):
    template_name = "back/artikel/artikel_tambah.html"
    article = Artikel.objects.get(id=id)
    if request.method == "POST":
        forms_artikel = ArtikelForms(request.POST, request.FILES, instance=article)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            print(request.user)
            art.nama = request.user
            art.save()
            return redirect(artikel)
    else:
        forms_artikel = ArtikelForms(instance=article)
    context = {
        'title':'Edit Artikel',
        'artikel':article,
        'forms_artikel':forms_artikel
    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request, id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

@api_view(['GET'])
def artikel_list(request, x_api_key):
    key = 'ilham'
    if key != x_api_key:
        content = {
            'status':False,
            'messages':'x api key tidak sama'
        }
        return Response(content)
    list = Artikel.objects.all()
    jumlah_artikel = list.count()
    serializer = ArtikelSerializer(list, many=True)
    content = {
        'status': True,
        'records': jumlah_artikel,
        'rows': serializer.data,
    }
    return Response(content)

@api_view(['GET', 'PUT', 'DELETE'])
def artikel_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        artikel = Artikel.objects.get(pk=pk)
    except Artikel.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArtikelSerializer(artikel)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArtikelSerializer(artikel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        artikel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)