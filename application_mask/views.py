import json

from django.shortcuts import render


def index(request):
    c = [{"name": "aaaaaaa", "url": "aaaaaaaaaaa"}, {"name": "bbbbbb", "url": "bbbbbbbb"}]
    context = {}
    context["items_json"] = json.dumps(c)
    return render(request, "application_mask/MainPage.html", context)

