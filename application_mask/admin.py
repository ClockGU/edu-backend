import io

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import TextFormat


from .models import Applicant
import zipfile


class ApplicantResource(resources.ModelResource):

    class Meta:
        model = Applicant


class ZIPCSV(TextFormat):
    TABLIB_MODULE = 'tablib.formats._csv'
    CONTENT_TYPE = 'application/zip'


class ZipExportModelAdmin(ImportExportModelAdmin):
    formats = [ZIPCSV]

    def get_export_filename(self, request, queryset, file_format):
        return "application_data.zip"

    def get_export_data(self, file_format, queryset, *args, **kwargs):
        export_inspector = super(ZipExportModelAdmin, self).get_export_data(file_format, queryset=queryset.filter(inspector_appl=True), *args, **kwargs)
        export_administartive = super(ZipExportModelAdmin, self).get_export_data(file_format, queryset=queryset.exclude(inspector_appl=True), *args, **kwargs)
        temp_file = io.BytesIO()
        with zipfile.ZipFile(
                temp_file, "w", zipfile.ZIP_DEFLATED
        ) as temp_file_opened:
            temp_file_opened.writestr(
                f"inspector_data.csv",
                io.BytesIO(bytes(export_inspector, "utf-8")).getvalue()
            )
            temp_file_opened.writestr(
                f"fami_VA_data.csv",
                io.BytesIO(bytes(export_administartive, "utf-8")).getvalue()
            )
        return temp_file.getvalue()


class ApplicantAdmin(ZipExportModelAdmin):
    resource_class = ApplicantResource


admin.site.register(Applicant, ApplicantAdmin)
