from django.urls import path
from .views import PostList, PostCreate, PostDelete, PostDetail, PostUpdate, SearchFormView

app_name = "post"

urlpatterns = [
    path("create/", PostCreate.as_view(), name='create'),
    path("delete/<int:pk>/", PostDelete.as_view(), name='delete'),
    path("update/<int:pk>/", PostUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", PostDetail.as_view(), name='detail'),
    path("", PostList.as_view(), name='index'),
    path("search/", SearchFormView.as_view(), name='search')
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)