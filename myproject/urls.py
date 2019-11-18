from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from core.views import home


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
