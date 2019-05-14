from django.conf import settings
from django.conf.urls.static  import static
from django.contrib import admin
from django.urls import path
from posts.views import blog, post, blog_home,  contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog_home),
    path('blog/',blog),
    path('post/',post),
    path('contact/',contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)