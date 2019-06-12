from django.conf import settings
from django.conf.urls.static  import static
from django.contrib import admin
from filebrowser.sites import site
from django.urls import path, include
from posts.views import (
    blog, post, blog_home,  about, search,
    post_create, post_update, post_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_home),
    path('blog/', blog, name='post-list'),
    path('create/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/update/', post_update, name='post-update'),
    path('post/<id>/delete/', post_delete, name='post-delete'),
    path('about/', about),
    path('search/', search, name='search'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
