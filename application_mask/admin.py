from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Applicant


class ApplicantResource(resources.ModelResource):

    class Meta:
        model = Applicant


class ApplicantAdmin(ImportExportModelAdmin):
    resource_class = ApplicantResource


admin.site.register(Applicant, ApplicantAdmin)
