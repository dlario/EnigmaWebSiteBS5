from django.contrib import admin
from django.urls import path, include
from aboutus import views
import aboutus

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', aboutus.views.home, name='navhome'),
                  path('accounts/', include('accounts.urls')),
                  path('aboutus/', include('aboutus.urls')),
                  path('equipment/', include('equipment.urls')),
                  path('inspections/', include('inspections.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
