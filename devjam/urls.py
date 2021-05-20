"""devjam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from converter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('index_search/', views.index_search, name='index_search'),
    path('search_engine/',views.search_engine, name="search_engine"),
    path('index_note/',views.index_note, name='index_note'),
    path('note_maker/', views.note_maker, name='note_maker'),
    # path('', include('converter.urls')),
    # path('index_convert/', views.index_convert, name='index_convert'),
    # path('imgtopdf/', views.imgtopdf),
    # path('doctopdf/', views.doctopdf),
]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
