from datetime import date

import environ
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"

    def validate(self, attrs):
        env = environ.Env()
        reg_start_date = date.fromisoformat(env.str("REG_START_DATE"))
        reg_end_date = date.fromisoformat(env.str("REG_END_DATE"))
        if not (reg_start_date <= date.today() <= reg_end_date):
            raise ValidationError("Die Anmeldung ist für dieses Jahr geschlossen.")
        return attrs


def map_true_false(dictionary):
    """
    Map Boolean values of a dict to True -> JA, False -> Nein
    :param dictionary:
    :return:
    """
    for key in dictionary:
        if not isinstance(dictionary[key], bool):
            continue
        dictionary[key] = "Ja" if dictionary[key] is True else "Nein"

    return dictionary