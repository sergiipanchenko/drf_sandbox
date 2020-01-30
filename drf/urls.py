from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),

    path('products/', include('apps.sandbox_1.urls')),
]
