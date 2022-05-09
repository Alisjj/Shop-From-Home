from django.contrib import admin
from django.urls import path, include
from products.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),

    #Local Apps
    path('accounts/', include('users.urls', namespace="users")),

    #Relord
    path("__reload__/", include("django_browser_reload.urls")),
]
