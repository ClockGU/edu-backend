from rest_framework import serializers
from .models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"

    def validate(self, attrs):
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