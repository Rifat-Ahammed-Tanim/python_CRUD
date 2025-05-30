from django.contrib import admin
from django.urls import path
from myapp.views import read, create, update, delete
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', read, name='read'),
    path('employee/create/', create, name='create'),
    path('employee/<int:id>/update/', update, name='update'),
    path('employee/<int:id>/delete/', delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
