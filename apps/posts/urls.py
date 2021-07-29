from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()
app_name = "posts"

router.register('',PostViewSet, basename="posts")


urlpatterns = router.urls

