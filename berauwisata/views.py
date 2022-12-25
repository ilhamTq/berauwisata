from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Artikel, Kategori
from user.models import Biodata

def index(request):
    template_name = 'frontend/index.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'Berau Wisata',
        'artikel':artikel,
    }
    
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = 'frontend/detail_artikel.html'
    artikel = Artikel.objects.get(id=id)
    context = {
        'title':'Artikel',
        'artikel':artikel
    }
    return render(request, template_name, context)
def about(request):
    template_name = 'frontend/about.html'
    context = {
        'title':'About'
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'frontend/contact.html'
    context = {
        'title':'Contact'
    }
    return render(request, template_name, context)

def blog(request):
    template_name = 'frontend/blog.html'
    artikel = Artikel.objects.all()
    kategori = Kategori.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(artikel, 6)
    try:
        artikel = paginator.page(page)
    except PageNotAnInteger:
        artikel = paginator.page(1)
    except EmptyPage:
        artikel = paginator.page(paginator.num_pages)
    context = {
        'title':'Our Blog',
        'artikel':artikel,
        'kategori':kategori,
    }
    
    return render(request, template_name, context)

def artikel_filter(request, nama):
    template_name = 'frontend/blog.html'
    kategori = Kategori.objects.all()
    artikel = Artikel.objects.filter(kategori__nama=nama)
    context = {
        'title':'Our Blog',
        'artikel':artikel,
        'kategori':kategori,
    }
    
    return render(request, template_name, context)

#LOGIN
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            pass
            print('username/password benar')
            auth_login(request, user)
            return redirect('index')
        else:
            pass
            print('username/password salah')
    context = {
        'title':'Form Login'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    template_name = "account/register.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')
        
        User.objects.create(
            username = username,
            password = make_password(password),
            first_name = nama_depan,
            last_name = nama_belakang,
            email = email,          
        )
        get_user = User.objects.get(username = username)
        Biodata.objects.create(
            user = get_user,
            alamat = alamat,
            telp = telp,
        )
        return redirect(index)
       
        
        
    context = {
        'title':'Form Registrasi',
    }
    return render(request, template_name, context)

def cuaca(request):
    template_name = "frontend/cuaca.html"
    context = {
        'title':'Cuaca'
    }
    
    return render(request, template_name, context)