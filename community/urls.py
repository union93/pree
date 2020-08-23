from django.conf.urls import url
from django.urls import path
from .views import CommunityList,CommunityCreate,CommunityDelete,CommunityUpdate,CommunityDetail,Communitysearch
app_name = "community"

urlpatterns = [
    path("", CommunityList.as_view(), name='index'),
    path("create/", CommunityCreate.as_view(), name='create'),
    path("delete/<int:pk>/", CommunityDelete.as_view(), name='delete'),
    path("update/<int:pk>/", CommunityUpdate.as_view(), name='update'),
    path("detail/<int:pk>/", CommunityDetail.as_view(), name='detail'),
    path("search/", Communitysearch, name='search')
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)