from django.conf import settings
from django.conf.urls.static  import static
from django.contrib import admin
from django.urls import path,url
from posts.views import blog, post, blog_home,  contact, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog_home),
    path('blog/', blog, name='post-list'),
    path('post/<id>/', post, name='post-detail'),
    path('contact/', contact),
    path('search/', search, name='search')
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
