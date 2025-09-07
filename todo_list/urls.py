from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks import views
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('tasks',views.TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api_token/', obtain_auth_token, name='api_token'),
]
