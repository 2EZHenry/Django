from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from todo.users.api.views import UserViewSet
from todo.todos.api.views import TodoViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("todos", TodoViewSet)


app_name = "api"
urlpatterns = router.urls
