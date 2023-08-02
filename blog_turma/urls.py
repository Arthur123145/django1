from django.urls import path, include
from . import views
from .forms import PostForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)