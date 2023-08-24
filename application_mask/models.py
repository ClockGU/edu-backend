from django.db import models


class Applicant(models.Model):

    firstname = models.CharField(max_length=200, verbose_name="Vorname")
    lastname = models.CharField(max_length=200, verbose_name="Nachname")
    email = models.EmailField(max_length=300, default="", verbose_name="Email")
    administrative_appl = models.BooleanField(null=True, blank=True, verbose_name="Verwaltungsfachangestellte*r")
    media_appl = models.BooleanField(null=True, blank=True, verbose_name="Fachangestellte*r für Medien- und Informationsdienste")
    inspector_appl = models.BooleanField(null=True, blank=True, verbose_name="Inspektoranwärter*in")
    soldier = models.BooleanField(null=True, blank=True, verbose_name="Soldat*in")
    disability = models.BooleanField(null=True, blank=True, verbose_name="Einschränkungen")

    class Meta:
        verbose_name = "Bewerber*in"
        verbose_name_plural = "Bewerber*innen"

    def __str__(self):
        return f"Bewerber: {self.firstname} {self.lastname}"
