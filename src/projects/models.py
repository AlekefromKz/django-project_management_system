from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="projects")
    title = models.CharField("Title", max_length=128)
    start_date = models.DateField("Start date", blank=True, null=True)
    end_date = models.DateField("End date", blank=True, null=True)

    estimated_hours = models.DecimalField("Estimated hours", max_digits=8, decimal_places=2)
    actual_hours = models.DecimalField("Actual hours", max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
