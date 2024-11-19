from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('merchants/', include('merchants.urls')),
    path('products/', include('products.urls')),
    path('categories/', include('categories.urls')),
    path('keywords/', include('keywords.urls')),
    path('promotions/', include('promotions.urls')),
    path('hashtags/', include('hashtags.urls')),
]
