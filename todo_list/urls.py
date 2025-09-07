from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views
router = DefaultRouter()
router.register('tasks',views.TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
