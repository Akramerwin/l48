from django.contrib import admin
from django.urls import path
from webapp.views import index_views, stufs_view, stuf_create, stuf_update_view, stuf_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views, name='index'),
    path('stufs/<int:pk>/', stufs_view, name='view'),
    path('create/', stuf_create, name='create'),
    path('stufs/<int:pk>/update', stuf_update_view, name='update'),
    path('stufs/<int:pk>/delete', stuf_delete_view, name='delete'),
]
