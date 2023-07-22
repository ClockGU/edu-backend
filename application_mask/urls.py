
from django.urls import path
from .views import index, SubmitView

urlpatterns = [
    path(r"", index, name="main-page"),
    path(r"submit", SubmitView.as_view(), name="submit")
]
