from django.contrib import admin
from django.urls import path, include

from projects.urls import company_urlpatterns, project_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include(company_urlpatterns)),
    path('project/', include(project_urlpatterns)),
]
