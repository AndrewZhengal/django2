"""supr_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from polls.views import index, detail
from news import views

urlpatterns = [
    path('', index),
    path('polls/<int:question_id>/', detail),

    path('blog/', views.blog_handler),
    path('single-blog/', views.single_blog_handler),
    path('archive/', views.archive_handler),
    path('category/', views.category_handler),
    path('contact/', views.contact_handler),
    path('index/', views.index_handler),
    path('robots.txt', views.robots_handler),

    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
