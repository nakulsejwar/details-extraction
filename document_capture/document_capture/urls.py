from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('document.urls')),
    path('api/', include('document.urls')),
    path('', TemplateView.as_view(template_name="frontend/index.html")),
]