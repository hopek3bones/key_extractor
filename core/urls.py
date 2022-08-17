"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="coditheck.guild@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
    # public=False,
    # permission_classes=(permissions.IsAdminUser, ),
);


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^apidoc/$',  schema_view.with_ui('redoc',   cache_timeout=0), name='schema-redoc'),
    path('api/', include('main.api'),   name="Main API"),
    path('',     include('main.views'), name="Main"),
];

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT);
