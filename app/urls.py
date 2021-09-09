from django.urls import path
from django.urls import path
from app import views
from app.views import upload, thisupload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload, name='file upload'),
    path('home/', views.thisupload, name='aaaaa')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)