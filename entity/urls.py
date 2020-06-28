from django.urls import path, include

from entity.apis import EntityViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('entities', EntityViewSet, basename='entity')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
