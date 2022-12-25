from django.contrib import admin
from django.urls import path, include
from berauwisata.views import *

################### -- Media -- ####################
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('filter/<str:nama>', artikel_filter, name='artikel_filter'),
    path('artikel/<int:id>/detail/', detail_artikel, name='detail_artikel'),
    path('blog/', blog, name='blog'),
    path('about-us/', about, name='about'),
    path('contact-us/', contact, name='contact'),
    path('cuaca/', cuaca, name='cuaca'),
    path('dashboard/', include('blog.urls')),
    path('dashboard/', include('user.urls')),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

################### -- Media -- ####################
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)