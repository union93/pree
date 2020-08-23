from django.contrib import admin
from django.templatetags.static import static
from django.urls import path,include

from pree import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('community/', include('community.urls'))
]
