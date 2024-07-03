from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('', include('home.urls')),  
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  
    path('book/', include('book.urls')),  
   
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)