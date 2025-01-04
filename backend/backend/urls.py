from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tag_tree_manager.urls')),  # Include app URLs
]
