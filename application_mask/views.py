import json

from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from application_mask.serializers import ApplicantSerializer


def index(request):
    c = [{"name": "aaaaaaa", "url": "aaaaaaaaaaa"}, {"name": "bbbbbb", "url": "bbbbbbbb"}]
    context = {}
    context["items_json"] = json.dumps(c)
    return render(request, "application_mask/index.html", context)


class SubmitView(CreateAPIView):
    serializer_class = ApplicantSerializer
