from rest_framework import serializers

from projects.models import Company, Project


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['company', 'title', 'start_date', 'end_date', 'estimated_hours', 'actual_hours']
