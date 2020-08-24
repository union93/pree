from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name ="main"
urlpatterns = [
    path('', views.index, name='first'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

