from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('about.html',views.about, name='about'),
    path('abouts', views.abouts_detail, name='abouts_detail'),
    path('checklist.html',views.todolist, name='checklist'),
    path('todo_detail/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('delete/<int:pk>/', views.deleteTask, name='delete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)