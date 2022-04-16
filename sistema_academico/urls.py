from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academico/', include('academico.urls')),
    path('', RedirectView.as_view(url='academico/', permanent=True)),
]
