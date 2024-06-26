from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mahsulotlar/', MahsulotlarAPIView.as_view()),
    # path('main/', include('main.urls')),
    # path('user/', include('user.urls')),
    # path('stats/', include('stats.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
