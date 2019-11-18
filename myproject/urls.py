from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'home.html', )


urlpatterns = [
    path('home', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls"))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
