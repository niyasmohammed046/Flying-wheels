from django.contrib import admin
from django.urls import path,include
import flyapp.urls
import frontend.urls
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('flyapp/',include(flyapp.urls)),
    path('',include(frontend.urls))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
