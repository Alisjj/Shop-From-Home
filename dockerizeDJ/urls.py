from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name="product_list"),

    # User management
    path('accounts/', include('allauth.urls')),

    #Local Apps
    path('accounts/', include('users.urls', namespace="users")),
    path('products/', include('products.urls', namespace="products")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('orders/', include('orders.urls', namespace="orders")),
    path('payment/', include('payment.urls', namespace="payment")),

    #Relord
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG == int(True):
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
