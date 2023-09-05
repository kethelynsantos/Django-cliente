from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_SAC.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('usuario', include('App_User.urls'))
]
