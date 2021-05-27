from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task_data', views.task_data_view),


urlpatterns = [
    path('', include(router.urls)),
]