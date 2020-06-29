from django.urls import path, include

from entity.apis import EntityViewSet, MultiTagSearchAPI

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("entities", EntityViewSet, basename="entity")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path(
        "api/entities/<str:tag>/",
        MultiTagSearchAPI.as_view(),
        name="multiterm_search_api",
    ),
]
