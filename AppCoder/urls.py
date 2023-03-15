from django.urls import path

from AppCoder.views import guardar_curso

urlpatterns = [
    path('curso/<camada>', guardar_curso),
]