from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Company, Project
from projects.serializers import CompanySerializer, ProjectSerializer


class CompanyRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListAPI(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateAPI(CreateAPIView):
    serializer_class = CompanySerializer


class ProjectRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectListAPI(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateAPI(CreateAPIView):
    serializer_class = ProjectSerializer


class CompanyProjectsAPI(APIView):
    def get(self, request, pk):

        projects = Company.objects.get(pk=pk).projects

        return Response(
            ProjectSerializer(projects, many=True).data,
            status=status.HTTP_200_OK
        )
