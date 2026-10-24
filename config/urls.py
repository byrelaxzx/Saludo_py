from django.urls import path, include

urlpatterns = [
    path("api/", include("saludo.infrastructure.web.urls")),
]