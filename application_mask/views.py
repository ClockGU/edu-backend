import json

from django.core.mail import EmailMessage
from django.shortcuts import render

from rest_framework.generics import CreateAPIView

from application_mask.serializers import ApplicantSerializer, map_true_false
from django.conf import settings


def index(request):
    c = [{"name": "aaaaaaa", "url": "aaaaaaaaaaa"}, {"name": "bbbbbb", "url": "bbbbbbbb"}]
    context = {}
    context["items_json"] = json.dumps(c)
    return render(request, "application_mask/index.html", context)


class SubmitView(CreateAPIView):
    serializer_class = ApplicantSerializer

    def post(self, request, *args, **kwargs):
        response = super(SubmitView, self).post(request, *args, **kwargs)
        self.send_mail(request, response.data)
        return response

    def send_mail(self, request, data):
        mapped_data = map_true_false(data)
        mapped_data["url"] = request.build_absolute_uri()
        message = EmailMessage(
            subject="Bewerbung erfolgreich!",
            body=self.format_message(mapped_data),
            from_email="GU Bewerberportal <{email}>".format(email=settings.SYSTEM_EMAILS["SENDER"]),
            to=[data["email"]],
            reply_to=[settings.SYSTEM_EMAILS["SENDER"]],
        )
        message.send(fail_silently=False)

    def format_message(self, data):
        text = (
            "Diese Daten wurden für Deine Bewerbung gespeichert:",
            f"Vorname: {data['firstname']}",
            f"Nachname: {data['lastname']}",
            f"E-Mail: {data['email']}",
            "",
            "Ausgewählte Berufe:",
            f"Verwaltungsfachangestellte*r (ab 01.08.2024): {data['administrative_appl']}",
            f"Fachangestellte*r für Medien- und Informationsdienste (ab 01.08.2024): {data['media_appl']}",
            f"Inspektoranwärter*in - Bachelor of Public Administation (ab 01.09.2024): {data['inspector_appl']}",
            "",
            "Nach Abschluss der Bewerbungsfrist erhältst Du von uns per Mail eine Einladung zu einem Online-Einstellungstest und weitere Informationen."
            "-----------------------",
            f"Dies ist eine automatisch generierte Nachricht des Bewerberportals für Auszubildende (System URL: {data['url']})",
        )

        return "\n".join(text)
