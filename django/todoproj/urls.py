from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from todoapi.views import ShopItemView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from todoapi import views as todoapi_views

router = routers.DefaultRouter()
router.register(
    'shop-item', ShopItemView, basename = 'shop-item'
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/task/', todoapi_views.RecepeeList.as_view(), name='task-list'),
    path('',include(router.urls)),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),

]
