from django.urls import path

from projects.apis import CompanyRetrieveUpdateDestroyAPI, CompanyListAPI, ProjectListAPI, \
    ProjectRetrieveUpdateDestroyAPI, CompanyCreateAPI, ProjectCreateAPI, CompanyProjectsAPI

company_urlpatterns = [
    path('', CompanyListAPI.as_view()),
    path('new/', CompanyCreateAPI.as_view()),
    path('<int:pk>/', CompanyRetrieveUpdateDestroyAPI.as_view()),
    path('<int:pk>/projects/', CompanyProjectsAPI.as_view()),
]

project_urlpatterns = [
    path('', ProjectListAPI.as_view()),
    path('new/', ProjectCreateAPI.as_view()),
    path('<int:pk>/', ProjectRetrieveUpdateDestroyAPI.as_view()),
]
